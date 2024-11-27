import cv2

class VideoProcessor:
    """Handles video input/output operations."""
    
    def __init__(self, config):
        self.config = config
        self.cap = None
        self.out = None
        
    def open_video(self):
        """Open input video and prepare output video writer."""
        self.cap = cv2.VideoCapture(self.config.video_path)
        
        # Get video properties
        self.frame_size = (
            int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Initialize video writer
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(
            self.config.output_path,
            fourcc,
            self.fps,
            self.frame_size
        )
        
        return self.frame_count
        
    def read_frame(self):
        """Read a frame from input video."""
        return self.cap.read()
        
    def write_frame(self, frame):
        """Write a frame to output video."""
        self.out.write(frame)
        
    def release(self):
        """Release video resources."""
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()