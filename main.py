def main():
    """Main application entry point."""
    # Initialize components
    config = Config()
    video_processor = VideoProcessor(config)
    data_processor = EyeTrackingDataProcessor(config)
    point_visualizer = PointVisualizer(config)
    
    try:
        # Setup
        frame_count = video_processor.open_video()
        data_processor.load_data()
        data_processor.initialize_processing(frame_count)
        
        # Main processing loop
        while True:
            ret, frame = video_processor.read_frame()
            if not ret:
                break
                
            # Get and update coordinates
            current, next_point = data_processor.get_coordinates(video_processor.frame_size)
            point_visualizer.update_points(current, next_point, video_processor.frame_size)
            
            # Process frame
            frame = point_visualizer.draw_points(frame)
            video_processor.write_frame(frame)
            
    finally:
        video_processor.release()
        print(f"Vidéo avec effet eye tracker enregistrée sous : {config.output_path}")

if __name__ == "__main__":
    main()