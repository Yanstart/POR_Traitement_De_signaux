import cv2
import numpy as np

class PointVisualizer:
    """Handles the visualization of eye tracking points on video frames."""
    
    def __init__(self, config):
        self.config = config
        self.current_point = None
        self.next_point = None
        
    def update_points(self, current, next_point, frame_size):
        """Update current and next points with smoothing."""
        if not self.current_point:
            self.current_point = (frame_size[0] // 2, frame_size[1] // 2)
            self.next_point = (frame_size[0] // 2, frame_size[1] // 2)
            
        if current:
            self.current_point = self._smooth_coordinates(self.current_point, current)
        if next_point:
            self.next_point = self._smooth_coordinates(self.next_point, next_point)
            
    def draw_points(self, frame):
        """Draw all points on the frame."""
        if not self._are_coordinates_valid(self.current_point, frame.shape):
            return frame
            
        frame = self._draw_point(frame, self.current_point, 'current')
        frame = self._draw_point(frame, self.next_point, 'next')
        frame = self._draw_path_points(frame)
        
        return frame
        
    def _smooth_coordinates(self, old_point, new_point):
        """Apply smoothing to coordinates."""
        factor = self.config.smoothing_factor
        x = int(factor * old_point[0] + (1 - factor) * new_point[0])
        y = int(factor * old_point[1] + (1 - factor) * new_point[1])
        return (x, y)
        
    def _draw_point(self, frame, point, point_type):
        """Draw a single point with blur effect."""
        if not self._are_coordinates_valid(point, frame.shape):
            return frame
            
        mask = frame.copy()
        mask[:] = 0
        
        cv2.circle(
            mask, point,
            self.config.points_config[point_type]['radius'],
            self.config.points_config[point_type]['color'],
            self.config.point_thickness
        )
        
        mask = cv2.GaussianBlur(mask, (21, 21), 0)
        return cv2.addWeighted(frame, 1.0, mask, 0.5, 0)
        
    def _draw_path_points(self, frame):
        """Draw interpolated points between current and next points."""
        for i in range(1, self.config.num_path_points + 1):
            interp_point = self._interpolate_point(i)
            if self._are_coordinates_valid(interp_point, frame.shape):
                frame = self._draw_point(frame, interp_point, 'path')
        return frame
        
    def _interpolate_point(self, i):
        """Calculate interpolated point position."""
        factor = i / (self.config.num_path_points + 1)
        x = int(self.current_point[0] + factor * (self.next_point[0] - self.current_point[0]))
        y = int(self.current_point[1] + factor * (self.next_point[1] - self.current_point[1]))
        return (x, y)
        
    def _are_coordinates_valid(self, point, frame_shape):
        """Check if coordinates are within frame boundaries."""
        return (point and 0 <= point[0] < frame_shape[1] and 
                0 <= point[1] < frame_shape[0])