**Dataset Description**

In this dataset, we are required to locate ships in images and place an aligned bounding box segment around the ships we locate. Many images do not contain ships, and those that do may contain multiple ships. Ships within and across images may differ in size (sometimes significantly) and be located in open sea, at docks, marinas, etc.

**Key Features:**

Non-overlapping Segments: For this metric, object segments cannot overlap. There were a small percentage of images in both the Train and Test sets that had slight overlap of object segments when ships were directly next to each other. Any segment overlaps were removed by setting them to background (i.e., non-ship) encoding. Therefore, some images have ground truth that may be an aligned bounding box with some pixels removed from an edge of the segment. These small adjustments will have a minimal impact on scoring, as the scoring evaluates over increasing overlap thresholds.

**About This File**

train_ship_segmentations.csv: This file provides the ground truth (in run-length encoding format) for the training images.
sample_submission.csv: This file contains the images in the test set.

**Sample Images:**
![00113a75c](https://github.com/tanuj437/ML-Crate/assets/128210429/b41182e5-7d70-4ee3-ad8a-23b22754f87d)
![00021ddc3](https://github.com/tanuj437/ML-Crate/assets/128210429/72a4683b-f8e3-44ea-adff-79b1c35c840e)
![008f038d3](https://github.com/tanuj437/ML-Crate/assets/128210429/a2f39df5-55a2-42da-8632-2ed0f32d8848)
![00aa79c47](https://github.com/tanuj437/ML-Crate/assets/128210429/5bf13a59-06e8-4b9e-a52e-9443d2814b41)







For more details and to access the dataset, visit the [Kaggle page](https://www.kaggle.com/competitions/airbus-ship-detection/data).
