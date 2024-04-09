# English

## Final Report Information

### Project Composition

- Groups of 1-3 are permitted. For groups of 3, additional work is required in the report beyond what is specified, such as extra graphs, more extensive discussion, and exploration of additional angles. However, this does not apply to the final project, which counts for 30% of the final grade.
- For pairs, expect to produce a report of approximately 4-6 pages including graphs. The report should be concise yet clear and well-presented. Both the code and the report equally contribute to the grade.

### Restrictions

- The use of ChatGPT or any similar AI tool, as well as copying code from the internet, is strictly prohibited. Everything must be your own work. Any discovery of code plagiarism or unauthorized assistance will result in a zero grade for the entire group.

### Submission Deadline

- The final submission is due over the weekend in the last week of instruction.

### Assignment Details

1. **Implementation of the K-means Algorithm in Python** for two datasets: MNIST and Fashion MNIST.

   a) **Data Input**: Import the data into the folder you are using in VSCode. Use the command `!pwd` in a code block to identify the folder location.

   b) **K-means Function**: Implement a kmeans function that takes data of length N and k. This function should return an np array of clusters, of size N x 1, with integers ranging from 0 to k-1, representing the classified category of each data point. Implement the necessary assign and update functions based on the pseudocode in section 3.6.

   - Start with initial points.
   - Iterate until convergence is achieved, with convergence criteria being either max_iterations or no change in data classification after the assign step.
     - Determine the best division - assign.
     - Determine new centroids - update.
   - Return the optimal division.

   c) **Visualization Functions**: Develop functions to plot the desired outcomes for inclusion in the report.

2. **The Report**: Can be composed in LaTeX, Word, or a Python notebook, but must be submitted as a PDF. It should not follow the same report format as previously used; no Python code executions or similar should be included.

### Report Structure and Content

- **Introduction**: Overview of the project.
- **Execution**: Description of the implementation process and a brief explanation of the algorithm.
- **Results**: Discussion on the outcomes and the performance of the implementation.
- **Code**: Include the used code, formatted neatly.

#### Topics to Cover

- Discuss the datasets and the K-means algorithm, its purpose, and why it's used.
- Advantages and disadvantages of K-means.
- Reasons for inaccurate classification.
- Any specific images that were misclassified more frequently.
- Performance differences between the two datasets, reasons for such differences, or lack thereof.

#### Required Graphs/Tables

- Histograms showing the distribution of your classification vs. the true classification.
- A table evaluating the effectiveness of your clustering. Helper functions will be provided for this purpose.
