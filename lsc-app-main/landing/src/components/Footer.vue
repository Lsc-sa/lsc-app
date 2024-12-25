<template>
  <footer
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="footer border-t bg-base-200 text-base-content p-10 flex flex-col items-center lg:flex-row lg:justify-evenly"
  >
    <div
      class="about-foot text-center flex flex-col items-center lg:max-w-80 lg:items-start"
    >
      <h2 class="text-2xl font-black">
        {{ $t("Footer.supportCenter.title") }}
      </h2>
      <p class="font-light lg:text-start">
        {{ $t("Footer.supportCenter.description") }}
      </p>
      <div class="footer-social-icons flex gap-4 mt-2">
        <a href="#">
          <font-awesome-icon
            icon="fa-brands fa-facebook-f"
            class="w-8 h-8 flex items-center justify-center duration-300 hover:scale-105"
          />
        </a>
        <a href="#">
          <font-awesome-icon
            class="w-8 h-8 flex items-center justify-center duration-300 hover:scale-105"
            icon="fa-brands fa-instagram"
          />
        </a>
        <a href="#">
          <font-awesome-icon
            class="w-8 h-8 flex items-center justify-center duration-300 hover:scale-105"
            icon="fa-brands fa-snapchat"
          />
        </a>
        <a href="#">
          <font-awesome-icon
            class="w-8 h-8 flex items-center justify-center duration-300 hover:scale-105"
            icon="fa-brands fa-x-twitter"
          />
        </a>
      </div>
    </div>
    <div
      class="text-center flex flex-col items-center lg:max-w-80 lg:items-start lg:text-start"
    >
      <h6 class="">
        {{ $t("Footer.supportCenter.contact.title") }}
      </h6>
      <p>
        {{ $t("Footer.supportCenter.contact.message") }}
      </p>
      <div class="flex flex-col mt-4">
        <!-- <p>
          <span class="font-bold">الرياض - الفرع الرئيسي:</span>
          شارع الأمير سعود بن عبد العزيز آل سعود الكبير - حي القدس - طريق
          الدائري الشرقي
          <br />
          <br />
          <span class="font-bold">جدة:</span>
          المكتب 416 - الطابق الرابع - مجمع عبد اللطيف بلازا، طريق الملك فهد
        </p> -->
        <a href="tel:0508062958">050-806-2958</a>
        <a href="mailto:info@lsc-sa.net">info@lsc-sa.net</a>
      </div>
    </div>
    <div class="flex flex-col items-center lg:max-w-80 lg:items-start">
      <h6 class="">
        {{ $t("Footer.company.title") }}
      </h6>
      <a href="#about" class="link link-hover">
        {{ $t("Footer.company.links.about") }}
      </a>
      <a href="#packages" class="link link-hover">
        {{ $t("Footer.company.links.packages") }}
      </a>
      <a href="#contact" class="link link-hover">
        {{ $t("Footer.company.links.contact") }}
      </a>
      <a class="link link-hover" onclick="my_modal_1.showModal()">
        {{ $t("Footer.company.links.termsAndConditions") }}
      </a>
      <a class="link link-hover" onclick="my_modal_11.showModal()">
        {{ $t("Footer.company.links.inquiriesPolicy") }}
      </a>
      <a class="link link-hover" onclick="my_modal_12.showModal()">
        {{ $t("Footer.company.links.returnPolicy") }}
      </a>
    </div>
  </footer>
  <footer class="footer ltr-footer bg-base-200">
    <div
      class="footer lg:w-4/5 lg:place-self-center text-base-content border-base-300 border-t px-10 py-4"
    >
      <aside
        class="flex flex-col justify-center items-center place-self-center text-center lg:flex-row lg:text-start lg:place-self-start lg:items-center lg:gap-4"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
          fill-rule="evenodd"
          clip-rule="evenodd"
          class="fill-current"
        >
          <path
            d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"
          ></path>
        </svg>
        <p>
          LSC Company.
          <br />
          Providing reliable law services since 2000.
        </p>
      </aside>
      <nav class="md:place-self-center md:justify-self-end place-self-center">
        <div class="grid grid-flow-col gap-4">
          <a href="#">
            <font-awesome-icon
              class="w-4 h-4 flex items-center justify-center duration-300 hover:scale-105"
              icon="fa-brands fa-x-twitter"
            />
          </a>
          <a href="#">
            <font-awesome-icon
              class="w-4 h-4 flex items-center justify-center duration-300 hover:scale-105"
              icon="fa-brands fa-snapchat"
            />
          </a>
          <a href="#">
            <font-awesome-icon
              icon="fa-brands fa-facebook-f"
              class="w-4 h-4 flex items-center justify-center duration-300 hover:scale-105"
            />
          </a>
          <a href="#">
            <font-awesome-icon
              class="w-4 h-4 flex items-center justify-center duration-300 hover:scale-105"
              icon="fa-brands fa-instagram"
            />
          </a>
        </div>
      </nav>
    </div>
  </footer>
  <footer class="lg:mb-0">
    <div class="copyrights-f text-center bg-base-200 py-4">
      <p>
        &copy; Copyright LSC 2024. | Design by
        <a href="https://www.linkedin.com/in/alil0l/" class="text-emerald-600"
          >Ali</a
        >
      </p>
    </div>
  </footer>
</template>

<style scoped>
.footer-title {
  color: white;
  opacity: 1;
}
.ltr-footer {
  direction: ltr;
}
</style>
<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>
