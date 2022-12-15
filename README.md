<link rel="icon" type="image/png" href="/assets/img/data.png" />
## Eat Sleep Data Repeat ⛺ 

[Data Driven Challenges for Organizations](https://hbr.org/2022/02/why-becoming-a-data-driven-organization-is-so-hard)\
![DM5](https://user-images.githubusercontent.com/75957662/200127239-f2346f45-be78-4734-93f6-28b5daba7351.jpeg)



### Tools/Technologies
---
1.Python\
2.Java\
3.SQL\
4.Pandas,PySpark,ConfigParser\
5.C++ (3D Objects)\
6.Google DataProc\
7.Google BigQuery
8.Google Cloud Storage\
9.Bash Scripting\
10.Distributed data processing(Apache Spark/Apache Hadoop)

### Self Reflection
I wanted to select three artifacts for my project that had personal significance for me. I wanted to choose projects which I would keep utilizing even after the requirements for this semester were finished, rather than ones that were just academic. I decided to concentrate on improving my e-portfolio, update code that I might use at work, and update a project to add functionality that would assist my growth.

For the software design and engineering portion of the project, I chose to apply what I learned in working with OpenGL library. In the class, we used these skills for a 3D animation, but for my final project I chose to apply them to my GitHub pages e-Portfolio. This project demonstrates my talents and ingenuity. In order to improve the design and make it more realistic in comparison to 2D things, I included a number of components. It shows off my ability to turn any 2D item into a 3D animation with a variety of characteristics.

For the algorithms and data structures part, I chose an artifact that was learned and completed in CS-260. It provided me with knowledge about how to approach a certain use case or problem. I started being familiar with numerous tools for writing manageable, performant code. I discovered how choosing the right data structure early on in the development of a program may improve data management and prevent issues like out of memory or stack overflow errors later on.
As I worked on the project, I discovered methods to leverage algorithms and data structures to increase its complexity and efficiency. This displays both my proficiency with algorithms and data structures and my proficiency with Python.

For the databases portion of the final project, I chose to apply what I learned in DAT-220 and created a cloud-based database. Assuming the company has a significant client base, I moved the data to a distributed file system. Using an open source framework, I enhanced data processing and schema enforcement beforehand so that the data science team could only utilize cleansed data while developing models.

### [Database enhancement]

The artifact I have selected for the database enhancement is form the course ‘DAT-220 Fundamentals of Data Mining’. This artifact used Microsoft JMP as its foundation to analyze the data and find the answers to the research questions aimed at creating business intelligence for the specified enterprise. JMP had not used data lake models. Assuming that client visits are increasing and that the outdated technology we were using cannot support the use case, we will now install lake house architecture. Since we were only saving files locally, the data storage size is where it initially fails. Second, the processing engine JMP has a set threshold for the volume of data it can handle, and third, none of the data was serialized, making it unsafe to store and process. This artifact used Microsoft JMP as its foundation to analyze the data and find the answers to the research questions aimed at creating business intelligence for the specified enterprise.


![DM4](https://www.waitingforcode.com/public/images/articles/lakehouse_architecture.png)


In order to adopt the Lakehouse architecture using the Google Cloud, we will first use Google Cloud Storage. The initial layer in this design is referred to as "raw_buppa_gump" and is also known as the bronze layer across industries. The layer keeps the storage data in its original, unprocessed state. The following layer, "silver_store_buppa gump", will include all of the curated data following the completion of the schema enforcement, maintain constraint, and data quality checks. This layer uses snappy compression to save the data in parquet format. This layer guarantees the effective storage of the data and improves the standard of the data that the business has uploaded in the bronze layer. This helps us to derive the models efficiently for the data science teams. We have the final layer as ‘report_store_buppa_gump’ which can be utilized by downstream system as a gold source or wherein we can put all the reports or models that has been created on top of ‘silve_store_buppa_gump’ data facilitates different departments of the company, to explore the specific states for the higher rate of income. the data science team will be able to generate the models utilizing various open source libraries to perform advance matrix generation and model creation which was not possible with JMP. Finally, we can also store the result back to our file system hosted in cloud which makes the storage more scalable, readily available across multiple counties and regions which was nearly impossible for JMP as it was performed in a local system. On top of that we also created a big query table which can be shared across multiple teams within the organization residing in various geographical region. With this enhancement, I learned a lot about the use of several open source tools to build a reliable and scalable data solution.

Despite being useful in helping us create a range of complicated models, the JMP framework lacked a reliable data storage and robust database system. During the enhancement, I found that the deployment of the cloud had made our database incredibly available and fault resilient, in contrast to the JMP and the data's local file system storage. A distributed architecture, which is practically impossible for systems that handle data vertically, allows us to efficiently grow any volume or type of data, as I also learned in between. Last but not least, JMP-like technologies are essentially unable to benefit from the polyglot programming nature that open source technology gives in order to curate scale migrate, and develop advanced KPI.  

![DM3](https://maelfabien.github.io/assets/images/gcp_32.jpg)

### [Algorithm enhancement]

![dM2](https://mymusing.co/wp-content/uploads/2017/04/sorting-time-complexity.jpg)

Data structures and algorithms were heavily emphasized in the foundational course for the Computer Science degree program, CS-260. CS-260 was the first programming course after a few others that really helped me understand the basics of data structures and algorithms. It not only provided me with knowledge about how to approach a specific use case or problem, but also with a number of tools for writing manageable, performant code. I discovered how choosing the right data structure early on in the development of a program can improve data management and prevent issues like out of memory or stack overflow exceptions later on. The course gave us a solid foundation in algorithms by introducing time and space complexity, showing us the many methods of problem resolution, and highlighting the most efficient ones.

In the CS-260 course, we talked about the sorting of vectors, which is a feature of the bid sorting algorithm. The data was extracted from a stream of bids submitted for real estate auctions in a municipal government data source. The provided information was saved locally in our local storage as a csv file at first. The application read the data from a local.csv file so that users could read it and sort it using our unique sorting method. One month's worth of data, or the monthly sales, might be sorted by the program. I sorted a vector that was essentially a collection of data on consumer bids for auction items using the "Selection Sort" method during the course. The selection sort process employed the technique of locating the smallest element of the vector and inserting it as the first element. The next step would include finding the second minimal value and moving it to the second position by conducting a loop from the second element of the vector to the last element. The loop keeps going until the Vector is sorted. Due to the tiny amount of data, this sorting method performed well for the Bid Sorting application. The algorithm's time complexity is O(n^2) and its space complexity is O (1).

As the enhancement to the above Bid Vector sorting program, I want to utilize the Quick Sort algorithms. I was planning on utilizing the Merge sort algorithm which has time complexity to O (n log(n)) and space complexity of O(n). As space has been the least factor, we consider in enterprise systems over the performance, I am opting in to use the Quick Sort algorithm over the Selection or Merge Sort that I explained in prior post. I came to learn that the utilization of caching helps the Quick Sort to be the most efficient over both Selection and Merge sort. The merge sort also utilizes the same approach of Divide and Conquer algorithm with O (n log(n)) time complexity and O(n^2) space complexity. I've discovered that the Quick Sort algorithm allows us to achieve the desired results faster than by just iterating through the complete list, array, or vector as in Selection sort. The Selection sort paradigm teaches us how to solve issues like sorting a vector with several passes based on a single value, where the number of passes is really equal to the number of items in the vector being sorted. I soon understood that selection sort was a better use case where memory was the primary issue. As I discovered for the majority of the sorting and searching procedures, memory hasn't been a significant issue in the modern technology industry, as we all know. Quicksort is frequently used and ought to be given preference over selection sort. It showed me when to utilize Divide and Conquer, Partition, and Recursive calls to simplify the procedure and improve the sorting in the background. As I researched the various sorting algorithms, I found that each one has benefits and drawbacks. Selection sort, despite being among the easiest to use, has the drawback of operating slowly, even on a partially sorted array. With regard to Quicksort, the cache-friendly algorithm had simplified and improved the search process without requiring any additional disk space.



---
[Data Driven need for Organizations](https://towardsdatascience.com/why-organizations-need-to-be-data-driven-98ade3ca53a)\
![dM2](https://user-images.githubusercontent.com/75957662/200127231-3c6d647c-420c-4893-a3f3-7512447b1d58.jpeg)


[MUST READ: DISTRIBUTED ARCHITECTURE](https://www.ionos.com/digitalguide/server/know-how/what-is-distributed-computing/)
