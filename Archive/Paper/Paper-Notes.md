# Efficient Classification of Very Large Images with Tiny Objects 

**Note:** These are points which are taken almost verbatim from the paper, just so that we can summarize the key points when starting the replication challenge.

## Problem Statement 
```
----- Motivated Challenges -----

1) Existing deep archirectures do not easily operate on large images (mega- or giga-pixels) due to memory constraints.

2) A very small fraction of the input images are informative of the label of interesting. This means that there is a low region of interest (ROI) to image ratio. 

This is problematic as most CNN architectures are designed for image classification datasets that have relatively large regions of interest and small image sizes (sub-megapixel)
```
## Main Idea 
- **Zoom-In Network:** An end-to-end CNN model that leverages **hierarchical attention sampling** for classification of large images with tiny objects. It only relies on a single GPU.
## Research Methodology
- The model is evaluated on four large-image datasets:
    1. Histopathy
    2. Road Scene 
    3. Satellite 
    4. Gigapixel Pathology
- Experimental results show that Zoom-In network architecture achieves higher accuracy than existing methods while requiring less memory resources.
## Experiments 
- 
## External References
- 