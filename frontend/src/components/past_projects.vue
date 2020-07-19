<template>
  <div>
    <div class="jumbotron dark-background">
        <h1 class="h1-responsive font-weight-bold text-center">Past Projects</h1>
        <div style="width: 75%; margin: 0 auto;">
            <p class="w-responsive text-center mx-0">There have been various projects I have took part in either as a side project, a hackthon entry or a school assignment. Below is a collection of the ones I am most fond of.</p>
        </div>
    </div>
    <div class="timeline">
      <div class="timeline-container left">
        <div class="content">
          <h3 class="h3-responsive">2020 - TauCeti</h3>
          <p>The latest side project undertaken, dreamt this up during 2019's T3 exam season.
          <br><br>The idea is to facilitate easier access for course materials, notes taken by alumnis and a general community forum for learning together
          <br><br>This project is current a work in progress, aiming for a 2020 T2 exam season launch</p>
          <p><small><a href="https://github.com/StevenShen1999/projectTauCeti" target="_blank">GitHub Link</a></small></p>
        </div>
      </div>
      <div class="timeline-container right">
        <div class="content">
          <h3 class="h3-responsive">2019 - Pointr</h3>
          <p>One of the many hackathons our team participated in 2019, this one was the UNSW Intercollege Hackathon and the theme was improving the lives of students living in on-campus accommodation. 
          <br><br>We managed to push out a MVP within 10 hours, using a Vue.js frontend and a Python/FLask/Postgres backend. 
          <br><br>Amazingly, we managed to win this one and are currently in the process of implementing this for production use for UNSW's Arc.</p>
          <p class="private"><small>GitHub Link not avaliable, private repo</small></p>
        </div>
      </div>
      <div class="timeline-container left">
        <div class="content">
          <h3 class="h3-responsive">2019 - Chibaba</h3>
          <p>The very first hackathon I participated in, 2019 CSESoc annual hackathon, and the theme was UN's sustainability goals.
          <br><br>We decided to focus on food waste and cooked up this project within 24 horus, written in a React frontend and a Python/Flask/SQLite backend.
          <br><br>This was also my first exposure to API designs using Python/Flask, must've read hours worth of documentation.</p>
          <p><small><a href="https://github.com/jysim3/chibaba" target="_blank">GitHub Link</a></small></p>
        </div>
      </div>
      <div class="timeline-container right">
        <div class="content">
          <h3 class="h3-responsive">2018 - Course Avaliability Scraper</h3>
          <p>A webscrapper written in Perl to notify users when a course they want to enrol in has a slot opening.</p>
          <p>Currently thinking about rewriting this script in Python</p>
          <p class="private"><small>GitHub Link not avaliable, private repo</small></p>
        </div>
      </div>
    </div> 
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
/* I claim no part of the css written below, all credits go to https://bootsnipp.com/snippets/O5q8E */
* {
  box-sizing: border-box;
}

/* Set a background color */
body {
  background-color: #474e5d;
  font-family: Helvetica, sans-serif;
}

/* The actual timeline (the vertical ruler) */
.timeline {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
}

/* The actual timeline (the vertical ruler) */
.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  background-color: white;
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -3px;
}

/* Container around content */
.timeline-container {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
  color: black;
}

/* The circles on the timeline */
.timeline-container::after {
  content: '';
  position: absolute;
  width: 25px;
  height: 25px;
  right: -12.5px;
  background-color: white;
  border: 4px solid black;
  top: 15px;
  border-radius: 50%;
  z-index: 1;
}

/* Place the container to the left */
.left {
  left: 0;
}

/* Place the container to the right */
.right {
  left: 50.3%;
}

/* Add arrows to the left container (pointing right) */
.left::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  right: 30px;
  border: medium solid white;
  border-width: 10px 0 10px 10px;
  border-color: transparent transparent transparent white;
}

/* Add arrows to the right container (pointing left) */
.right::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  left: 30px;
  border: medium solid white;
  border-width: 10px 10px 10px 0;
  border-color: transparent white transparent transparent;
}

/* Fix the circle for containers on the right side */
.right::after {
  left: -16px;
}

/* The actual content */
.content {
  padding: 20px 30px;
  background-color: black;
  position: relative;
  border-radius: 6px;
  color: white;
}

/* Media queries - Responsive timeline on screens less than 600px wide */
@media screen and (max-width: 600px) {
/* Place the timelime to the left */
  .timeline::after {
    left: 31px;
  }

/* Full-width containers */
  .timeline-container {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;
  }

/* Make sure that all arrows are pointing leftwards */
  .timeline-container::before {
    left: 60px;
    border: medium solid white;
    border-width: 10px 10px 10px 0;
    border-color: transparent white transparent transparent;
  }

/* Make sure all circles are at the same spot */
  .left::after, .right::after {
    left: 15px;
  }

/* Make all right containers behave like the left ones */
  .right {
    left: 0%;
  }
}

a {
  text-decoration: none;
  color: inherit;
}

.private:hover {
  cursor: not-allowed;
}
</style>