class Config:
    """Configuration for the eye tracking visualization."""
    
    def __init__(self):
        # Video paths
        self.video_path = "assets/Test Your Awareness.avi"
        self.data_path = "assets/DataPOR.csv"
        self.output_path = "assets/Output_Video_With_Points.avi"
        
        # Resolution mapping
        self.source_resolution = (1600, 1050)
        
        # Point visualization settings
        self.points_config = {
            'current': {'color': (0, 0, 255), 'radius': 20},  # Rouge
            'next': {'color': (0, 255, 0), 'radius': 15},     # Vert
            'path': {'color': (255, 0, 0), 'radius': 15}      # Bleu
        }
        self.point_thickness = -1
        self.num_path_points = 10
        self.smoothing_factor = 0.8