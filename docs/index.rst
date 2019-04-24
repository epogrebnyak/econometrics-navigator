.. Econometrics Navigator documentation master file, created by 
   sphinx-quickstart on Fri Nov 16 05:36:08 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 1
   
   topics/index.rst
   textbook/index.rst
   how-to-teach/index.rst
   data.md
   software.rst
   blogs.md
   tweets.md 
   acronyms.md

Welcome to Econometrics Navigator!
==================================

Goals
-----

The Econometrics Navigator (EN) aims to enable easier learning and coding 
for statistics and econometrics by dowing two things:

- guide a learner through **open access textbooks**  and **community knowledge** (reddit, Stack Overflow, Cross Validated, twitter threads) 

- illustrate key topics with **minimal code examples** in open source software 
  (Python, R, gretl or Julia).

Changelog
---------

- **v.0.0.2 (November 2018)** original version of EN nobody understood what it is good for,
  had sample articles on max likelihood, bootstrap, ANOVA.

- **v.0.0.3 (April 2019)** scraps several unfinished articles, including 
  a section on applications (hard to fill it quickly). Three main parts
  in content established (own articles, textbook annotations and how to 
  teach resources).

Content
-------

1. Collection of own articles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main body of Econometrics Navigator articles is `Concepts and techniques section <topics/index.rst>`__,  organised alphabetically. Finished examples are: 

- `Maximum likelihood <topics/max-likelihood.html>`__
- `Bootstrap <topics/bootstrap.html>`__
- `ANOVA <topics/anova.html>`__ 

2. Textbooks guide  
~~~~~~~~~~~~~~~~~~

`Textbooks review <textbook/index.html>`__ attempts to sort out and annotate textbooks and 
reference texts by several categories. 

For example, I praise Kennedy's textbook and 
collect (constructive) criticisms of Mostly Harmless Econometrics there. The categories 
in econometrics are 'general' textbooks, cross-section/panel and time series texts.

3. Instructor resources
~~~~~~~~~~~~~~~~~~~~~~~

The backstage workings of the Navigator are `History of econometrics <history.html>`__, 
`Ways to review econometrics <how-to-teach/ways-into-econometrics.html>`__ and 
`econometrics mindmap (draft) <how-to-teach/mindmap.html>`__. 

These documents aim to organise thinking about better teaching of 
econometrics in terms of sequence of topics, better analogies for the learner and 
a faster bridge to coding from formulas. 

Roadmap 
-------

In next versions, I would like to do the following:

-  draw a mindmap for econometrics, the one that is just described in  text and put key textbooks on it
-  write more articles for the main section
-  review 'depreciated' folder, and 'history' page
-  add resources on reproducible research and why it has such a poor traction in economics
-  add APIs to Data section and a lightbulb survival case, which is dear to me
-  pick couple resources on (technical) pedagogy - how to teach effectively
-  pay more attention to bayesian / causality
-  'vednorize' `LessOLS <https://github.com/epogrebnyak/LessOLS.jl>`__
-  add a bit more of `deep learning links <https://github.com/epogrebnyak/learn/blob/master/deep_learning.md>`__
-  things mentioned in `todo.txt <https://github.com/epogrebnyak/econometrics-navigator/blob/master/todo.txt>`__


Links (reproducibility):

-  `this <https://github.com/epogrebnyak/notes-pandoc/blob/master/paper.md>`__
-  `this <https://github.com/epogrebnyak/notes-pandoc>`__ 

Links (teaching):

-  https://twitter.com/AllenDowney/status/1118255413575680000
-  http://teachtogether.tech/en/

Twitter 
-------

So far twitter has been an enormously valuable source of demos, links and opinion for me.
I keep a `separate page with twitter posts <tweets.html>`__, some of my favorites are:

- `Undergrad Econometrics Cheatsheet <https://twitter.com/tyleransom/status/1085242403643183105>`__ by Tyler Ransom

.. raw:: html

    <embed>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Also, in case it&#39;s useful, here is an entire overview of undergrad econometrics (no matrix algebra) in 3 pages: <a href="https://t.co/kQYrn92v7w">https://t.co/kQYrn92v7w</a> <a href="https://t.co/UBe7OZJTJh">pic.twitter.com/UBe7OZJTJh</a></p>&mdash; Tyler Ransom (@tyleransom) <a href="https://twitter.com/tyleransom/status/1085242403643183105?ref_src=twsrc%5Etfw">January 15, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
    </embed>

- `Casual graphs and XY plane animations <http://nickchk.com/causalgraphs.html>`__ by Nick Huntington-Klein

.. raw:: html

    <embed>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">As requested, slower graphs! Also added a graph on collider bias, the webpage explanation helps there.<br><br>These graphs are intended to show what standard causal inference methods actually *do* to data, and how they work.<br><br>This is what controlling for a binary variable looks like: <a href="https://t.co/dTZxqY5JxA">pic.twitter.com/dTZxqY5JxA</a></p>&mdash; Nick HK (@nickchk) <a href="https://twitter.com/nickchk/status/1068215492458905600?ref_src=twsrc%5Etfw">November 29, 2018</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
    </embed>

- `Investigative time series example <https://twitter.com/PogrebnyakE/status/1111897245362909185>`__ by @cubic_logic 

.. raw:: html

    <embed>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Two series. Find which one is a random walk. <a href="https://t.co/IC8QxzhVND">pic.twitter.com/IC8QxzhVND</a></p>&mdash; (λ --- --. .. -.-.)³ (@cubic_logic) <a href="https://twitter.com/cubic_logic/status/1111346696754249730?ref_src=twsrc%5Etfw">March 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
    </embed>

- `Common statistical tests are linear models (or: how to teach stats) <https://lindeloev.github.io/tests-as-linear>`__ by Jonas Kristoffer Lindeløv

.. raw:: html

    <embed>
    <blockquote class="twitter-tweet"><p lang="en" dir="ltr">I&#39;ve made this cheat sheet and I think it&#39;s important. Most stats 101 tests are simple linear models - including &quot;non-parametric&quot; tests. It&#39;s so simple we should only teach regression. Avoid confusing students with a zoo of named tests. <a href="https://t.co/9PFR1ly3lW">https://t.co/9PFR1ly3lW</a> 1/n</p>&mdash; Jonas K. Lindeløv (@jonaslindeloev) <a href="https://twitter.com/jonaslindeloev/status/1110907133833502721?ref_src=twsrc%5Etfw">March 27, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
    </embed>


Contacts
--------

Feel free to contact me `@PogrebnyakE <https://twitter.com/PogrebnyakE>`__.
I need help in shaping this guide.

Source
------

The source of this publication is available at https://github.com/epogrebnyak/econometrics-navigator.
