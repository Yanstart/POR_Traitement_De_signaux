# POR_Traitement_De_signaux

## Objective

This project processes eye-tracking data to overlay the Point of Regard (POR) on a video and generate a heatmap summarizing the zones most (or least) frequently viewed. The main goal is to enhance visualization and understanding of gaze data.

## Minimum Viable Product (MVP)

1. **Overlay the Point of Regard (POR)**:  
   Add a visual tag to a video indicating the subject's gaze point using provided data.

2. **Smooth Gaze Movements**:  
   Filter eye-tracking data to reduce saccades and create smoother transitions for better visualization.

3. **Generate a Heatmap**:  
   At the end of the video, produce a heatmap image highlighting gaze frequency across different zones.

## Workflow

### 1. Input Files
- **Video file**: The base video viewed by the subject.  
- **CSV file**: Gaze data including coordinates corresponding to the subject's viewing patterns.

Place these files in the `assets` folder of the repository.

### 2. Processing
- The notebook reads the video and gaze data.
- Applies smoothing filters to the gaze data for smoother visual representation.
- Overlays the gaze points on each frame of the video.

### 3. Output
- **Processed Video**: A new video with the POR overlaid.  
- **Heatmap**: A separate image file representing zones based on gaze frequency.

Both outputs are saved in the `assets` folder.

## How to Use

### Requirements
- Python 3.8+
- Jupyter Notebook
- Libraries: `opencv-python`, `numpy`, `matplotlib`, `pandas`, `seaborn`

### Steps
1. Clone the repository:
    ```bash
    git clone [<repository_url>](https://github.com/Yanstart/POR_Traitement_De_signaux/)
    cd POR_Traitement_De_signaux
    ```
2. Add the input files (`video` and `csv`) to the `assets` folder.
3. Open the Jupyter Notebook:
    ```bash
    jupyter notebook auto_filter_heatMap2.ipynb
    ```
4. Execute the notebook sequentially to process the video and generate outputs.

## Data Sources
This project utilizes data provided by:
- **Mathieu Petieau** (mathieu.petieau@ulb.be)  
  Université Libre de Bruxelles (ULB)

Supervised by:
- **Arnaud Dewulf** (a.dewulf@ephec.be)  
  EPHEC

## Upcoming Features
- **Demo**: A demonstration video showcasing the tool’s capabilities will be added soon.

## Contact
For questions or contributions, feel free to open an issue or contact me (the developer) directly.
