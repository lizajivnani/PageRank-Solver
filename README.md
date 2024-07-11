<h1 align="left">Project Overview </h1>


<p align="left"> Ever wonder how Google decides which websites to show you first? That's what PageRank is all about! Check out this version of the PageRank algorithm. It's like creating a mini search engine that figures out which web pages are the most important. We'll use two different methods to do this:

1) Pretending to be a random internet surfer
2) Using some cool math to calculate importance scores.

</p>



<h3 align="left">Random Surfer Model</h3>




![image](https://github.com/user-attachments/assets/a32f1446-1d79-4e6f-b003-452d0c10db80)

<br><br><br>


<h3 align="left">Iterative Algorithm</h3>



![image](https://github.com/user-attachments/assets/e2a5f460-d87a-4740-b99f-7d0d39f23a04)



It's a fun way to peek behind the curtain of how search engines work. Let's dive in and rank some pages!

<h1 align="left">Features </h1>


Implementation of the PageRank algorithm using two methods:
1) Random Surfer Model
2) Iterative Algorithm

Project Structure:

pagerank.py: Main Python script containing the PageRank implementation
corpus0/, corpus1/, corpus2/: Sample web page corpora for testing

Key Functions:

1) transition_model(corpus, page, damping_factor): Returns a probability distribution over which page to visit next.
2) sample_pagerank(corpus, damping_factor, n): Estimates PageRank values using the Random Surfer Model.
3) iterate_pagerank(corpus, damping_factor): Calculates PageRank values using the iterative formula method.


Usage:
>> python pagerank.py [corpus]


Acknowledgments:
This project is part of Harvard University's CS50 Introduction to Artificial Intelligence with Python, ©2024 Harvard University.

