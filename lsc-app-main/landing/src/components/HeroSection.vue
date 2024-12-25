<template>
  <section class="header" id="home" :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'">
    <div
      class="hero w-full px-4 min-h-screen lg:min-h-full 3xl:min-h-screen lg:justify-start mt-20 lg:mt-28 lg:px-40"
    >
      <div class="hero-content gap-20 flex-col text-center text-white">
        <div class="hero-text flex flex-col gap-8 lg:items-start">
          <h3 class="text-2xl font-bold">{{ $t("HeroSection.title") }}</h3>
          <h1 class="text-4xl lg:text-start text-center font-semibold">
            {{ $t("HeroSection.titleTextp1") }}
            <br />
            {{ $t("HeroSection.titleTextp2") }}
          </h1>
          <p class="max-w-2xl text-light text-justify text-sm">
            {{ $t("HeroSection.heroBriefp1") }}
            <br />
            {{ $t("HeroSection.heroBriefp2") }}
          </p>
        </div>
        <div class="btns flex flex-col gap-4 w-full lg:flex-row lg:gap-8">
          <a
            href="https://portal.lsc-sa.net/dashboard"
            class="btn bg-primary w-full lg:w-1/2 text-white border-primary border-4 hover:text-white hover:bg-primaryHover hover:border-primaryHover"
          >
            {{ $t("Signup") }}
            <img
              width="24"
              height="24"
              src="https://img.icons8.com/parakeet-line/24/FFFFFF/user.png"
              alt="user"
            />
          </a>
          <button
            onclick="my_modal_2.showModal()"
            class="btn bg-primary w-1/2 lg:w-1/4 text-white border-primary border-4 hover:text-white hover:bg-primaryHover hover:border-primaryHover"
          >
            {{ $t("Early Register") }}
            <img
              width="24"
              height="24"
              src="https://img.icons8.com/parakeet-line/24/FFFFFF/user.png"
              alt="user"
            />
          </button>
        </div>
        <div class="side-links hidden gap-4">
          <ul class="home-social-list">
            <li>
              <a href="#"
                ><img
                  width="25"
                  height="25"
                  src="https://img.icons8.com/ios/25/FFFFFF/facebook--v1.png"
                  alt="facebook--v1"
              /></a>
            </li>
            <li>
              <a href="#"
                ><img
                  width="25"
                  height="25"
                  src="https://img.icons8.com/ios/25/FFFFFF/twitterx--v1.png"
                  alt="twitterx--v1"
              /></a>
            </li>
            <li>
              <a href="#"
                ><img
                  width="25"
                  height="25"
                  src="https://img.icons8.com/ios/25/FFFFFF/instagram-new--v1.png"
                  alt="instagram-new--v1"
              /></a>
            </li>
            <li>
              <a href="#"
                ><img
                  width="25"
                  height="25"
                  src="https://img.icons8.com/ios/25/FFFFFF/snapchat--v1.png"
                  alt="snapchat--v1"
              /></a>
            </li>
          </ul>
          <!-- end home-social-list -->

          <div class="home-scrolldown">
            <a href="#about" class="scroll-icon scroll-smooth">
              <span class="flex flex-row-reverse gap-2"
                >Scroll Down
                <img
                  aria-hidden="true"
                  class="p-2 bg-white rounded-full"
                  width="24"
                  height="24"
                  src="https://img.icons8.com/material-rounded/48/chevron-right.png"
                  alt="chevron-down"
                />
              </span>
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-img"></div>
  </section>
</template>

<style scoped>
.bg-img {
  display: flex;
  position: absolute;
  bottom: -200px;
  z-index: -10;
  justify-content: center;
  align-self: center;
  width: 100%;
  height: 200%;
  background-position: center;
  background-image: url("../assets/images/bg.jpg");
  background-size: cover;
  filter: blur(4px) brightness(0.5);
}

.home-social-list {
  position: absolute;
  left: 42px;
  top: 35%;
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 2.2rem;
  line-height: 1.75;
  text-align: center;
  -webkit-transform: translateY(-55%);
  -ms-transform: translateY(-55%);
  transform: translateY(-55%);
}

.home-social-list::before {
  display: block;
  content: "";
  width: 2px;
  height: 42px;
  background-color: rgba(255, 255, 255, 0.15);
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 12px;
}

.home-social-list li {
  padding-left: 0;
}

.home-social-list li a,
.home-social-list li a:visited {
  color: #ffffff;
}

.home-social-list li a:hover,
.home-social-list li a:focus,
.home-social-list li a:active {
  color: #223458;
}

/* scroll down */

.home-scrolldown {
  position: absolute;
  top: 0;
  left: 0;
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
  -webkit-transform-origin: left bottom;
  -ms-transform-origin: left bottom;
  transform-origin: left bottom;
  float: left;
}

.home-scrolldown i {
  padding-left: 9px;
}

.home-scrolldown a:hover,
.home-scrolldown a:focus {
  color: #223458 !important;
}

html[data-useragent*="MSIE 10.0"] .home-scrolldown,
.oldie .home-scrolldown {
  display: none;
}

.scroll-icon {
  display: inline-block;
  font-family: "montserrat-medium", sans-serif;
  font-size: 1rem;
  text-transform: uppercase;
  letter-spacing: 0.3rem;
  color: #ffffff !important;
  background: transparent;
  position: relative;
  bottom: 36px;
  left: 350px;
  -webkit-animation: animate-it 3s ease infinite;
  animation: animate-it 3s ease infinite;
}

.scroll-icon i {
  font-size: 2.4rem;
  position: relative;
  top: -6px;
}

/* vertical animation */

@-webkit-keyframes animate-it {
  0%,
  60%,
  80%,
  100% {
    -webkit-transform: translateX(0);
  }
  0%,
  60%,
  80%,
  100% {
    transform: translateX(0);
  }
  20% {
    -webkit-transform: translateX(-5px);
  }
  20% {
    transform: translateX(-5px);
  }
  40% {
    -webkit-transform: translateX(20px);
  }
  40% {
    transform: translateX(20px);
  }
}

@keyframes animate-it {
  0%,
  60%,
  80%,
  100% {
    -webkit-transform: translateX(0);
  }
  0%,
  60%,
  80%,
  100% {
    transform: translateX(0);
  }
  20% {
    -webkit-transform: translateX(-5px);
  }
  20% {
    transform: translateX(-5px);
  }
  40% {
    -webkit-transform: translateX(20px);
  }
  40% {
    transform: translateX(20px);
  }
}

@media only screen and (max-width: 1300px) {
  .home-image-right {
    left: 5rem;
  }
}

@media only screen and (max-width: 1200px) {
  #home {
    overflow: hidden;
  }
  .home-content {
    vertical-align: middle;
  }
  .home-content-left {
    padding: 18rem 0 12rem 40px;
  }
  .home-content-left h3 {
    font-size: 1.5rem;
  }
  .home-content-left h1 {
    font-size: 4.8rem;
  }
  .home-image-right {
    padding-bottom: 18rem;
  }
  .home-image-right img {
    vertical-align: bottom;
    width: 70%;
  }
}

@media only screen and (max-width: 1100px) {
  .home-content-left h1 {
    font-size: 4.6rem;
  }
  .home-content-left h1 br {
    display: none;
  }
}

@media only screen and (max-width: 1024px) {
  .home-content-left {
    width: 60%;
    padding: 18rem 6rem 12rem 4rem;
  }
  .home-content-left h3 {
    font-size: 1.5rem;
  }
  .home-content-left h1 {
    font-size: 4.2rem;
  }
  .home-image-right {
    width: 40%;
    padding-top: 120px;
  }
  .home-image-right img {
    vertical-align: top;
    width: 100%;
  }
}

@media only screen and (max-width: 900px) {
  #home {
    height: auto;
    min-height: 840px;
  }
  #home,
  .home-content {
    display: block;
    text-align: center;
  }
  .home-content-left {
    width: 94%;
    position: static;
    padding: 15rem 6rem 366px;
    margin: 0 auto;
  }
  .home-content-left h1 {
    margin-bottom: 3.6rem;
  }
  .home-image-right {
    width: 400px;
    left: auto;
    bottom: auto;
    right: 50%;
    top: 0;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
    padding: 0;
    margin-top: -378px;
  }
}

@media only screen and (max-width: 768px) {
  #home {
    min-height: auto;
  }
  .home-content-left h3 {
    font-size: 1.4rem;
  }
  .home-content-left h1 {
    font-size: 3.6rem;
  }
}

@media only screen and (max-width: 600px) {
  .home-content-left {
    padding: 12rem 6rem 366px;
  }
  .home-content-left h1 {
    font-size: 3.3rem;
  }
  .home-content-left .button.stroke {
    width: 100%;
    min-width: 0;
    max-width: 280px;
  }
  .home-social-list {
    font-size: 2rem;
    left: 30px;
  }
  .scroll-icon {
    bottom: 21px;
  }
}

@media only screen and (max-width: 500px) {
  .home-social-list,
  .home-scrolldown {
    display: none;
  }
  .home-content-left {
    padding: 12rem 2.5rem 366px;
    width: 100%;
  }
  .home-content-left h1 {
    font-size: 3rem;
  }
}

@media only screen and (max-width: 400px) {
  .home-content-left {
    padding: 12rem 0 300px;
  }
  .home-content-left .button.stroke {
    margin: 0 0 1.2rem 0;
  }
  .home-image-right {
    width: 320px;
    margin-bottom: -298px;
  }
}
</style>
