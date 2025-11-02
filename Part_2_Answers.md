
# Part 2: Reasoning-Based Questions

---

Q1: Choosing the Right Approach
I would use object detection because the goal is to locate where the product label is missing, not just to say whether it exists or not. Object detection can identify both the presence and exact position of the label on each product. If this fails to capture fine details (like partially missing labels), my fallback would be image segmentation, which gives pixel-level precision.

---

### Q2: Debugging a Poorly Performing Model
To debug a poorly performing model, I would first inspect whether the dataset is balanced between classes. Next, I would visualize some of the predictions and compare them to the ground truth to see if labeling errors exist. I would also analyze the training and validation loss curves for overfitting or underfitting and test augmentation or fine-tuning. Checking lighting variations, backgrounds, and camera angles in new factory images can also reveal data distribution mismatches.

---

### Q3: Accuracy vs Real Risk
Accuracy is not the best metric for this case, because even a small number of missed defective products can be dangerous or costly. Instead, I would focus on **recall** (how many defective products are correctly identified) and **precision** (how many detected defects are truly defects). A better metric would be **F1-score** or **false negative rate**, since missing one defective product can have a real-world safety or financial impact.

---

### Q4: Annotation Edge Cases
Blurry or partially visible objects should be **partially kept** if they realistically represent what the model will see in production. Including them improves robustness in real-world conditions but can make training harder. If the model must work on factory cameras that sometimes produce blur, keeping them is essential. The trade-off is between clean learning vs. realistic generalization — I’d include representative but high-quality blurry samples.
