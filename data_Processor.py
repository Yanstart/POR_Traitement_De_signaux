import pandas as pd
import numpy as np

class EyeTrackingDataProcessor:
    """Handles loading and processing of eye tracking data."""
    
    def __init__(self, config):
        self.config = config
        self.data = None
        self.frame_count = 0
        self.current_row = 0
        self.increment = 0
        
    def load_data(self):
        """Load and prepare eye tracking data from CSV."""
        self.data = pd.read_csv(
            self.config.data_path, 
            delimiter='\t', 
            encoding='utf-8', 
            low_memory=False
        )
        self.eye_data = self.data.loc[1:, ["L POR X [px]", "L POR Y [px]"]]
        
    def initialize_processing(self, frame_count):
        """Initialize processing parameters based on video frame count."""
        self.frame_count = frame_count
        self.increment = len(self.eye_data) / frame_count
        
    def get_coordinates(self, target_resolution):
        """Get current and next coordinates, scaled to target resolution."""
        if int(self.current_row) >= len(self.eye_data) - 2:
            return None, None
            
        current = self._scale_coordinates(
            self.eye_data.iloc[int(self.current_row)],
            target_resolution
        )
        next_point = self._scale_coordinates(
            self.eye_data.iloc[int(self.current_row) + 2],
            target_resolution
        )
        
        self.current_row += self.increment
        return current, next_point
        
    def _scale_coordinates(self, point_data, target_resolution):
        """Scale coordinates from source to target resolution."""
        x = float(point_data["L POR X [px]"]) / self.config.source_resolution[0] * target_resolution[0]
        y = float(point_data["L POR Y [px]"]) / self.config.source_resolution[1] * target_resolution[1]
        return (int(x), int(y))
