<template>
  <section
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="testimonials w-full px-4 min-h-screen lg:min-h-full 3xl:min-h-screen flex flex-col justify-center"
    id="testimonials"
  >
    <SectionTitle :title="t('Reviews')" />
    <div
      class="testimonials-cards flex items-center flex-col gap-8 justify-center mt-8"
    >
      <div class="carousel w-full">
        <div
          id="slide1"
          class="carousel-item relative w-full flex justify-center items-center"
        >
          <div
            class="testimonials-card flex flex-col items-center justify-center max-w-3xl shadow-sm bg-white px-4 py-6 rounded-2xl"
          >
            <div class="img-c w-20 mb-4">
              <img
                width="100"
                height="100"
                src="https://img.icons8.com/bubbles/100/user.png"
                alt="user"
              />
            </div>
            <h2 class="font-bold mb-4 text-3xl">
              {{ $t("ReviewsSection.testimonial1.name") }}
            </h2>
            <p class="text-center font-light mb-4">
              {{ $t("ReviewsSection.testimonial1.testimonial") }}
            </p>
            <div class="rate flex gap-2">
              <img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              />
            </div>
          </div>
          <div
            class="absolute left-5 right-5 top-1/4 flex -translate-y-1/2 transform justify-between"
          >
            <a
              href="#slide4"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❮</a
            >
            <a
              href="#slide2"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❯</a
            >
          </div>
        </div>
        <div
          id="slide2"
          class="carousel-item relative w-full flex justify-center items-center"
        >
          <div
            class="testimonials-card flex flex-col items-center justify-center max-w-3xl shadow-sm bg-white px-4 py-6 rounded-2xl"
          >
            <div class="img-c w-20 mb-4">
              <img
                width="100"
                height="100"
                src="https://img.icons8.com/bubbles/100/user.png"
                alt="user"
              />
            </div>
            <h2 class="font-bold mb-4 text-3xl">
              {{ $t("ReviewsSection.testimonial2.name") }}
            </h2>
            <p class="text-center font-light mb-4">
              {{ $t("ReviewsSection.testimonial2.testimonial") }}
            </p>
            <div class="rate flex gap-2">
              <img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              />
            </div>
          </div>
          <div
            class="absolute left-5 right-5 top-1/4 flex -translate-y-1/2 transform justify-between"
          >
            <a
              href="#slide1"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❮</a
            >
            <a
              href="#slide3"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❯</a
            >
          </div>
        </div>
        <div
          id="slide3"
          class="carousel-item relative w-full flex justify-center items-center"
        >
          <div
            class="testimonials-card flex flex-col items-center justify-center max-w-3xl shadow-sm bg-white px-4 py-6 rounded-2xl"
          >
            <div class="img-c w-20 mb-4">
              <img
                width="100"
                height="100"
                src="https://img.icons8.com/bubbles/100/man-with-beard-in-suit.png"
                alt="man-with-beard-in-suit"
              />
            </div>
            <h2 class="font-bold mb-4 text-3xl">
              {{ $t("ReviewsSection.testimonial3.name") }}
            </h2>
            <p class="text-center font-light mb-4">
              {{ $t("ReviewsSection.testimonial3.testimonial") }}
            </p>
            <div class="rate flex gap-2">
              <img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              />
            </div>
          </div>
          <div
            class="absolute left-5 right-5 top-1/4 flex -translate-y-1/2 transform justify-between"
          >
            <a
              href="#slide2"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❮</a
            >
            <a
              href="#slide4"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❯</a
            >
          </div>
        </div>
        <div
          id="slide4"
          class="carousel-item relative w-full flex justify-center items-center"
        >
          <div
            class="testimonials-card flex flex-col items-center justify-center max-w-3xl shadow-sm bg-white px-4 py-6 rounded-2xl"
          >
            <div class="img-c w-20 mb-4">
              <img
                width="100"
                height="100"
                src="https://img.icons8.com/bubbles/100/user.png"
                alt="user"
              />
            </div>
            <h2 class="font-bold mb-4 text-3xl">
              {{ $t("ReviewsSection.testimonial4.name") }}
            </h2>
            <p class="text-center font-light mb-4">
              {{ $t("ReviewsSection.testimonial4.testimonial") }}
            </p>
            <div class="rate flex gap-2">
              <img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              /><img
                width="48"
                height="48"
                src="https://img.icons8.com/fluency/48/star--v1.png"
                alt="star--v1"
              />
            </div>
          </div>
          <div
            class="absolute left-5 right-5 top-1/4 flex -translate-y-1/2 transform justify-between"
          >
            <a
              href="#slide3"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❮</a
            >
            <a
              href="#slide1"
              class="btn btn-circle bg-transparent border-transparent md:bg-primary md:border-primary"
              >❯</a
            >
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>
