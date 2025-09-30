import os
import numpy as np

class MSTAR:
    """
    A custom class to load MSTAR target data and assign labels.
    """
    def __init__(self, data_dir):
        """
        Initializes the MSTAR data loader.

        Args:
            data_dir (str): The path to the directory containing the MSTAR target subfolders.
        """
        self.data_dir = data_dir
        self.classes = self._get_class_names()
        self.class_to_idx = {cls_name: i for i, cls_name in enumerate(self.classes)}
        self.idx_to_class = {i: cls_name for cls_name, i in self.class_to_idx.items()}
        self.data, self.labels = self._load_data()

    def _get_class_names(self):
        """
        Retrieves class names (labels) from subfolder names.
        """
        return sorted([d for d in os.listdir(self.data_dir) if os.path.isdir(os.path.join(self.data_dir, d))])

    def _load_data(self):
        """
        Loads the MSTAR data and assigns numerical labels.
        (This is a simplified example; actual data loading logic may vary).
        """
        all_data = []
        all_labels = []
        print(f"Found {len(self.classes)} target classes: {self.classes}")

        for class_name in self.classes:
            class_path = os.path.join(self.data_dir, class_name)
            for filename in os.listdir(class_path):
                # This is where you would load your data file (e.g., a SAR image)
                # For this example, we'll just use the filename as a placeholder.
                file_path = os.path.join(class_path, filename)

                # Assign the label based on the folder name
                label = self.class_to_idx[class_name]

                all_data.append(file_path) # Storing file paths instead of raw data
                all_labels.append(label)
        """
        # Shuffle the data
        combined = list(zip(all_data, all_labels))
        np.random.shuffle(combined)
        shuffled_data, shuffled_labels = zip(*combined)
         
        return np.array(shuffled_data), np.array(shuffled_labels)
        """
    def get_labels(self):
        """Returns the numerical labels."""
        return self.labels

    def get_class_names(self):
        """Returns the human-readable class names."""
        return self.classes


# --- Example Usage ---
if __name__ == "__main__":
    # Specify the path to your MSTAR dataset
    # For this example, we'll assume a local directory named 'mstar_dataset'

    DATASET_PATH = r'C:/Users/mitch/Documents/PAMSAR/SAMPLE_dataset_public-master/mat_files/real'
    # Instantiate the class
    mstar_loader = MSTAR(DATASET_PATH)

    # Get the data and labels
    file_paths = mstar_loader.data
    labels = mstar_loader.get_labels()


