<script setup>
import AboutSection from ".././components/AboutSection.vue";
import HeroSection from ".././components/HeroSection.vue";
import ServiceSection from ".././components/ServiceSection.vue";
import Footer from ".././components/Footer.vue";
import ContactSection from ".././components/ContactSection.vue";
import PricingSection from ".././components/PricingSection.vue";
import Testimonials from ".././components/Testimonials.vue";
import TopNav from ".././components/TopNav.vue";
import { ref, onMounted } from "vue";

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

onMounted(() => {
  const cookieConsent = getCookie("userAcceptedCookies");
  if (!cookieConsent) {
    hideNow.value = false;
  } else {
    hideNow.value = true;
  }
});

const hideNow = ref(false);
function handleClick(isAccepted) {
  hideNow.value = true;

  if (isAccepted) {
    // User accepted cookies, create a new cookie
    document.cookie = "userAcceptedCookies=true; path=/; max-age=31536000"; // Cookie lasts 1 year (31536000 seconds)
  } else {
    // User rejected cookies, delete all cookies
    document.cookie.split(";").forEach(function (c) {
      document.cookie =
        c.trim().split("=")[0] +
        "=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    });
  }
}
</script>

<template>
  <TopNav />
  <HeroSection />
  <div class="bg-slate-200 text-black relative">
    <AboutSection />
    <ServiceSection />
    <PricingSection />
    <!-- <Testimonials /> -->
    <ContactSection />
    <div
      :class="[
        'cookiesNote fixed bottom-4 left-4 rounded-lg bg-white text-black',
        hideNow ? 'hidden' : '',
      ]"
    >
      <div class="card rounded-lg bg-white text-black w-80 max-w-screen">
        <div class="card-body items-center text-center">
          <h2 class="card-title">{{ $t("Cookies") }}</h2>
          <p>{{ $t("CookiesMsg") }}</p>
          <div class="card-actions justify-end">
            <button class="btn btn-primary" @click="() => handleClick(true)">
              {{ $t("Accept") }}
            </button>
            <button class="btn btn-ghost" @click="() => handleClick(false)">
              {{ $t("Deny") }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <Footer />
</template>
