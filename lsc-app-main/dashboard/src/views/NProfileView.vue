<template>
  <LoggedInTopNav :title="t('Personal Information')" :backArrow="false" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24 max-w-96 mx-auto"
  >
    <RouterLink :to="{ name: 'UserSettingsView' }">
      <Loader v-if="loadingCurrent" />
      <div v-else class="brief flex gap-4">
        <img
          :src="userData?.user_image || ProfilePic"
          alt="ProfilePic"
          class="w-1/2 max-w-24 block rounded-lg"
        />
        <div class="brief-info text-xs flex flex-col justify-evenly">
          <h2 class="text-black font-bold">{{ userData?.full_name }}</h2>
          <p class="font-medium">
            {{ $t("ID Number") }}
            :
            <span>{{ userData?.custom_id_number }}</span>
          </p>
        </div>
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'PersonalinfoView' }">
      <div class="personalInfo flex justify-between items-center">
        <div class="rig flex gap-2">
          <img :src="Profile" alt="ProfileIcon" />
          <p class="text-black">
            {{ $t("Personal Information") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'ResidentialinfoView' }">
      <div class="accomInfo flex justify-between items-center">
        <div class="rig flex gap-2">
          <img :src="HomeHash" alt="HomeIcon" />
          <p class="text-black">
            {{ $t("Residence Information") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'PowerofAttView' }">
      <div class="accomInfo flex justify-between items-center">
        <div class="rig flex gap-2 items-center text-black">
          <font-awesome-icon icon="fa-regular fa-file" class="w-6 h-6" />
          <p class="text-black">
            {{ $t("Attach Authorization") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'AllInvoicesView' }">
      <div class="accomInfo flex justify-between items-center">
        <div class="rig flex gap-2 items-center text-black">
          <font-awesome-icon icon="fa-regular fa-credit-card" class="w-6 h-6" />
          <p class="text-black">
            {{ $t("Previous Invoices") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'AccountStatusPage' }">
      <div class="accomInfo flex justify-between items-center">
        <div class="rig flex gap-2 items-center text-black">
          <font-awesome-icon
            icon="fa-regular  fa-address-book"
            class="w-6 h-6"
          />
          <p class="text-black">
            {{ $t("Account Status") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <RouterLink :to="{ name: 'ContactUs' }">
      <div class="accomInfo flex justify-between items-center">
        <div class="rig flex gap-2 items-center text-black">
          <font-awesome-icon icon="fa-solid  fa-question" class="w-6 h-6" />
          <p class="text-black">
            {{ $t("Contact Us") }}
          </p>
        </div>
        <img
          :src="$i18n.locale == 'ar' ? LeftArrowBlack : LeftArrow"
          alt="Icon"
        />
      </div>
    </RouterLink>
    <div class="terms flex justify-between">
      <RouterLink :to="{ name: 'InquiriesPolicy' }">
        <div class="accomInfo flex justify-between items-center">
          <div class="rig flex gap-2 items-center text-primary">
            <p class="text-primary">
              {{ $t("Inquiries Policy") }}
            </p>
          </div>
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'ReturnPolicy' }">
        <div class="accomInfo flex justify-between items-center">
          <div class="rig flex gap-2 items-center text-primary">
            <p class="text-primary">
              {{ $t("Return Policy") }}
            </p>
          </div>
        </div>
      </RouterLink>
    </div>
    <div class="terms flex justify-between">
      <RouterLink :to="{ name: 'TermsView' }">
        <div class="accomInfo flex justify-between items-center">
          <div class="rig flex gap-2 items-center text-primary">
            <p class="text-primary">
              {{ $t("Terms of Use") }}
            </p>
          </div>
        </div>
      </RouterLink>
      <div></div>
      <!-- <RouterLink :to="{ name: 'PrivacyPolicy' }">
        <div class="accomInfo flex justify-between items-center">
          <div class="rig flex gap-2 items-center text-primary">
            <p class="text-primary">
              {{ $t("Privacy Policy") }}
            </p>
          </div>
        </div>
      </RouterLink> -->
    </div>

    <div class="accomInfo flex justify-between items-center">
      <label class="label cursor-pointer w-full text-black">
        <span class="label-text">
          {{ $t("Language") }}
        </span>
        <div class="flex gap-2">
          <!-- <span class="label-text">عربي</span>  -->
          <input
            type="checkbox"
            class="toggle bg-white"
            :checked="!isArabic"
            @change="toggleLanguage"
          />
          <!-- <span class="label-text">English</span> -->
        </div>
      </label>
    </div>
  </div>
  <Loader v-if="loading" />
  <BottomNav />
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
const currentLocale = ref(locale.value);

import BottomNav from "@/components/BottomNav.vue";
import { RouterLink } from "vue-router";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import Profile from "../assets/images/icons/profile.svg";
import LeftArrowBlack from "../assets/images/icons/LeftArrowBlack.svg";
import LeftArrow from "../assets/images/icons/arrow_back_black.svg";
import HomeHash from "../assets/images/icons/home-hashtag.svg";
import ProfilePic from "../assets/images/profile.png";
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import Loader from "@/components/Loader.vue";
import axios from "axios";
import { useQuery } from "@tanstack/vue-query";

const loading = ref(false);

const navigate = useRouter();
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};

fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
  .then((response) => {
    if (!response.ok) {
      throw new Error("You are not logged In");
    }
    return response.json();
  })
  .then()
  .catch(() => navigate.replace("/"));

const userData = ref({
  full_name: "",
  custom_id_number: "",
  user_image: "",
  language: "",
});

const isArabic = ref(true);
const toggleLanguage = async () => {
  // Call your API to switch language
  const selectedLang = isArabic.value ? "en" : "ar"; // Toggle between Arabic and English
  locale.value = isArabic.value ? "en" : "ar";

  // Set language in localStorage
  localStorage.setItem("language", locale.value);

  // Set language in cookies (cookie will expire in 1 year)
  document.cookie = `language=${locale.value}; path=/; max-age=${
    60 * 60 * 24 * 30 * 12
  }`;

  const formData = new FormData();
  formData.append("language", selectedLang);
  try {
    loading.value = true;
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.update_user_data.update_user_data",
      {
        method: "PATCH",
        body: formData, // Send the formData
      }
    );
  } catch (error) {
    console.error("Error changing language:", error);
  } finally {
    setTimeout(() => {
      loading.value = false;
    }, 500);
  }

  // Toggle language state
  isArabic.value = !isArabic.value;
};

const getUserData = () =>
  axios.get("/api/method/lsc_api.lsc_api.get_user_data.get_user_data");

const { data: userDataQ, isLoading: loadingCurrent } = useQuery({
  queryKey: ["userDataQ"],
  queryFn: getUserData,
});

const refreshData = () => {
  userData.value = userDataQ?.value?.data?.message?.user_data;
  if (userData.value?.language == "en") {
    isArabic.value = false;
  }
  if (userData.value?.full_name) {
    localStorage.setItem("loader", true);
  }
};
// const getUserData = async () => {
//   try {
//     const response = await fetch(
//       "/api/method/lsc_api.lsc_api.get_user_data.get_user_data"
//     );
//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }
//     const data = await response.json();
//     userData.value = data.message.user_data;
//     if (userData.value.language == "en") {
//       isArabic.value = false;
//     }
//   } catch (error) {
//     console.error("Error fetching user data:", error);
//   }
// };

onMounted(() => {
  refreshData();
  if (locale.value == "en" || localStorage.getItem("language") == "en") {
    isArabic.value = false;
  } else {
    isArabic.value = true;
  }
  if (localStorage.getItem("loader") != "true") {
    loading.value = true;
    setTimeout(() => {
      refreshData();
      localStorage.removeItem("loader");
      loading.value = false;
    }, 2000);
  } else {
    localStorage.removeItem("loader");
  }
});
</script>
