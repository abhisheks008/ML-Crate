<h1>Hand Pose Detection</h1>
<br>
<h2>GOAL</h2>
<br>
<h2>Write the main goal of project and what's the purpose of it.</h2>
<p>Detect hand from the image.</p>
<br>
<a href="https://www.kaggle.com/rupakroy/handpose-detection"><h2>DATASET</h2></a>
<br>
<h2>DESCRIPTION</h2>
<p>The ability to perceive the shape and motion of hands can be a vital component in improving the user experience across a variety of technological domains and platforms.

MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame. Whereas current state-of-the-art approaches rely primarily on powerful desktop environments for inference, our method achieves real-time performance on a mobile phone, and even scales to multiple hands.</p>
<p>
    <ul>
        <li>Import mediapipe hand detector.</li>
        <li>Set parameters to the model.</li>
        <li>Pass image to the model.</li>
        <li>Position of the 21 coordinates of the hand and bbox arounf the hand is returned by the model.</li>
    </ul>
</p>
</br>
<h2>MODELS USED</h2>
<p><strong>Palm Detection Model: </strong>The method addresses challenges using different strategies. First, a palm detector is trianed instead of a hand detector, since estimating bounding boxes of rigid objects like palms and fists is significantly simpler than detecting hands with articulated fingers. In addition, as palms are smaller objects, the non-maximum suppression algorithm works well even for two-hand self-occlusion cases, like handshakes. Moreover, palms can be modelled using square bounding boxes (anchors in ML terminology) ignoring other aspect ratios, and therefore reducing the number of anchors by a factor of 3-5. Second, an encoder-decoder feature extractor is used for bigger scene context awareness even for small objects (similar to the RetinaNet approach). Lastly, we minimize the focal loss during training to support a large amount of anchors resulting from the high scale variance.</p>
<p><strong>Hand Landmark Model: </styrong>After the palm detection over the whole image our subsequent hand landmark model performs precise keypoint localization of 21 3D hand-knuckle coordinates inside the detected hand regions via regression, that is direct coordinate prediction. The model learns a consistent internal hand pose representation and is robust even to partially visible hands and self-occlusions. To obtain ground truth data, ~30K real-world images are annoated with 21 3D coordinates, as shown below (we take Z-value from image depth map, if it exists per corresponding coordinate). To better cover the possible hand poses and provide additional supervision on the nature of hand geometry, we also render a high-quality synthetic hand model over various backgrounds and map it to the corresponding 3D coordinates.</p>
<br>
<h2>LIBRARIES NEEDED</h2>
<p>
    <ul>
        <li>mediapipe: For hand detection model published by Google.</li>
        <li>matplotlib: For visualization.</li>
        <li>opencv: For image processing</li>
        <li>os: moving from one  folder to other</li>
    </ul>
</p>
<br>
<h2>VISUALIZATION</h2>
<p>All the outputs can be found in the image folder.</p>
<br>
<h2>ACCURACIES<h2>
<p>An average precision of 95.7% in palm detection. Using a regular cross entropy loss and no decoder gives a baseline of just 86.22%.</p>
<br>
<h2>CONCLUSION</h2>
<p>The model is performing very good to localize and identify hands. Beside the handDetector class also be used for detect hands from images and videos and all the parameters can be modified easily.</p>
<br>
<h2>Contributor: </h2>
<br>
<ul>
    <li><strong>Ankur Das</strong></li>
    <li><strong>LinkedIn: </strong>https://www.linkedin.com/in/ankur-das-145b13157/</li>
    <li><strong>GitHub: </strong>https://github.com/das-ankur</li>
</ul>
<br>