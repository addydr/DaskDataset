# DaskDataset
COP4521: Secure, Parallel, and Distributed Programming Module 14
<h2>Description</h2>
This project leverages Dask to efficiently process and analyze a large dataset through parallel computing. In the computer script, Dask loads the data into a dataframe so that the data can be grouped by one columns while computing an aggregate over another. In the visualize script, Dask and Graphviz are used to visualize the Directed Acyclic Graph (DAG) that represents the computation. 


<h4>Key Highlights:</h4>

- Parallel Computing: Demonstrates the power of parallel computing for handling large-scale data operations. Dask intelligently partitions the dataset into smaller Pandas DataFrames, enabling concurrent processing and optimizing memory usage.

- Data Analysis: The script efficiently loads and processes the dataset, allowing for advanced grouping and aggregation tasks, showcasing Dask's ability to handle complex data manipulations with ease.

- DAG Visualization: The visualize script uses Dask and Graphviz to create a clear and informative visualization of the DAG, providing insights into the computation workflow and task dependencies.

This project showcases efficient parallel computing techniques for handling large operations. Here, Dask loads the data set into several smaller Pandas dataframes on a need basis, allowing for concurrent computing.

<h4>Note:</h4> The .csv used is too large to upload. It was found at this link: https://catalog.data.gov/dataset/crime-data-from-2020-to-present


<br />


<h2>Languages and Utilities Used</h2>

- <b>Python 3</b>
- <b>Dask</b>
- <b>Graphviz</b>
- <b>Pandas</b>

<h2>Environments Used </h2>

- <b>PyCharm</b>

<h2>Program walk-through:</h2>

<p align="center">
In PyCharm, run the compute script to compute the crime data. Here, you can see the compute times with ProgressBar, and the interpreted data: <br/>
<img src="https://i.imgur.com/b9hUdGE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Next, run the vizualize script to generate the DAG for the crime data computation:  <br/>
<img src="https://i.imgur.com/wkJk8aL.png" height="80%" width="80%" alt="Step1"/>
<br />
<br />
Now, you can view the generated DAG images. Here is Max Age by Weapon: <br/>
<img src="https://i.imgur.com/KoEXt7R.png" height="80%" width="80%" alt="Step2"/>
<br />
<br />
Min Age by Weapon:  <br/>
<img src="https://i.imgur.com/XzY1fa7.png" height="80%" width="80%" alt="Step3"/>
<br />
<br />
Mean Age by Weapon:  <br/>
<img src="https://i.imgur.com/yE4B2aH.png" height="80%" width="80%" alt="Step4"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
