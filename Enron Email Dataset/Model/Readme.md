## Enron email dataset.

This dataset was collected and prepared by the CALO Project (A Cognitive Assistant that Learns and Organizes). It contains data from about 150 users, mostly senior management of Enron, organized into folders. 

The corpus contains a total of about 0.5M messages. This data was originally made public, and posted to the web, by the Federal Energy Regulatory Commission during its investigation. The email dataset was later purchased by Leslie Kaelbling at MIT, and turned out to have a number of integrity problems. 

A number of folks at SRI, notably Melinda Gervasio, worked hard to correct these problems, and it is thanks to them (not me) that the dataset is available. The dataset here does not include attachments, and some messages have been deleted "as part of a redaction effort due to requests from affected employees.


## In this dataset the procedure followed is:
1. Having a glance at the dataset.
2. Reducing the size of the dataset.
3. Analysing the sender.
4. Counting the frequency.
5. Create df with 2 highest emails. 
6. Preprocessing and get ready for machine learning
7. Remove rare words
8. Define X and y
9. Split for training and validating
10. Vectorise
11. Define and train model
12. Predict on validation set
13. Evaluate
