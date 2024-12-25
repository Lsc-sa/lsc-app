<template>
  <LoggedInTopNav :title="t('Authorizations')" :backArrow="true" />
  <div class="flex flex-col sm:flex-row w-full px-6 gap-5 mt-24 lg:mt-40 pb-24">
    <div
      class="card bg-white rounded-box flex-grow px-4 py-10 gap-10 shadow-md"
    >
      <div v-if="subscriptionStat" class="ele text-black text-center">
        <h1 class="font-bold">
          {{ $t("Create an authorization via Najiz") }}
        </h1>
        <p>{{ $t("Representative Data") }}</p>
        <ul>
          <li>
            {{ $t("Name") }}
            :
            <span @click="copyClip"> نايف بن داوود بن صالح العتيق </span>
          </li>
          <li>
            {{ $t("ID Number") }}
            :
            <span @click="copyClip"> 1014288417 </span>
          </li>
          <li>
            {{ $t("Date of Birth") }}
            :
            <span @click="copyClip"> 20/11/1396 </span>
            -
            <span @click="copyClip"> 12/11/1976 </span>
          </li>
          <li>
            {{ $t("Phone Number") }}
            :
            <span @click="copyClip"> 0559957083 </span>
          </li>
          <li>
            {{ $t("Representative") }}
            :
            {{ $t("Lawyer") }}
          </li>
          <li>
            {{ $t("Follow the following instructions from Najiz") }}
            <br />
            <RouterLink
              :to="{
                path: '/profile/allInvoices/AnewPrint',
                query: {
                  invoice:
                    'https://new.najiz.sa/applications/landing/e-services/3472d517-7cb4-4cd5-a6bc-2abc9751eea3',
                },
              }"
              target="_blank"
              class="text-primary text-center"
            >
              {{ $t("Here") }}
            </RouterLink>
            <span class="px-4">
              {{ t("Or") }}
            </span>
            <RouterLink
              :to="{
                path: '/profile/allInvoices/AnewPrint',
                query: {
                  invoice:
                    'https://www.youtube.com/embed/St3KeHU4xjs?si=MGHpJupVqBbLuriQ',
                },
              }"
              target="_blank"
              class="text-primary text-center"
            >
              {{ $t("Youtube") }}
            </RouterLink>
          </li>
        </ul>
      </div>
      <!-- Form Start -->
      <button
        class="btn btn-primary text-white border-white bg-primary text-white w-full max-w-40 self-center"
        @click.prevent="toggleDisable"
        :class="allowEdit ? 'bg-danger' : ''"
      >
        {{ allowEdit ? $t("Undo") : $t("Edit") }}
      </button>
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
        <!-- Buttons for Save and Edit -->
        <button
          class="btn btn-success text-white w-full max-w-40 self-center"
          type="submit"
          :class="allowEdit ? '' : ' hidden'"
        >
          {{ $t("Save Changes") }}
        </button>
        <div class="flex flex-col gap-4">
          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Najiz Authorization Number") }}
                </span>
              </div>
              <input
                type="tel"
                maxlength="9"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.attonery_number__najiz"
                :disabled="!allowEdit"
              />
            </label>
          </div>
          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Authorization Expiration Date") }}
                </span>
              </div>
              <VueDatePicker
                v-model="userData.expiry_date"
                :enable-time-picker="false"
                range-separator="-"
                :min-date="minDate"
                :disabled="!allowEdit"
              />
            </label>
          </div>
          <div
            class="imgtwo relative flex justify-center"
            @click="allowEdit ? triggerFiletwo() : null"
          >
            <img
              :src="userData.file[0]?.attachments || id_face"
              alt="التوكيل"
              class="w-1/2 max-w-60 w-full block rounded-2 max-h-52"
            />
            <div
              v-if="allowEdit"
              class="absolute top-0 left-0 w-full h-full bg-gray-800 bg-opacity-75 flex items-center justify-center cursor-pointer"
            >
              <font-awesome-icon
                icon="fa-solid fa-file-circle-plus"
                class="text-black"
              />
            </div>
            <!-- Hidden File Input -->
            <input
              type="file"
              ref="filetwo"
              accept="image/*, .pdf, .doc, docx"
              class="hidden"
              @change="handleFileChangeback"
            />
          </div>
          <font-awesome-icon
            v-if="changeIcon"
            class="text-black w-8 h-8"
            icon="fa-solid fa-circle-check"
          />
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="mt-4 p-4 bg-red-100 text-red-800 border border-red-300 rounded"
        >
          {{ errorMessage }}
        </div>
      </form>
      <!-- Form End -->
    </div>
  </div>
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import showToastMessage from "../router/toastmessage";

import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import id_face from "@/assets/images/id_front.png";
const showToast = ref(false);
const toastMessage = ref(null);
const navigate = useRouter();
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};
const changeIcon = ref(null);
const allowEdit = ref(false);
const loading = ref(false);
const minDate = new Date();
const errorMessage = ref(""); // Error message state
const filetwo = ref(null);
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
  attonery_number__najiz: "",
  expiry_date: "",
  file: [""],
});

const triggerFiletwo = () => {
  filetwo.value.click();
};

const toggleDisable = () => {
  allowEdit.value = !allowEdit.value;
  if (!allowEdit.value) getAttorney();
};

const handleFileChangeback = (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  changeIcon.value = true;
  reader.onload = (e) => {
    userData.value.file = e.target.result;
    reader.readAsDataURL(file);
  };
};

const convertDate = (date) => {
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, "0");
  const month = String(d.getMonth() + 1).padStart(2, "0");
  const year = String(d.getFullYear()).slice(-2);
  return `${year}-${month}-${day}`;
};

// Validation function
const validateForm = () => {
  if (
    !userData.value.attonery_number__najiz ||
    !userData.value.expiry_date ||
    !filetwo.value
  ) {
    errorMessage.value = t("All fields are required"); // Error message in Arabic
    return false;
  } else if (userData.value.attonery_number__najiz.length != 9) {
    errorMessage.value = t("Najiz Number Must be 9 numbers");
    return false;
  }
  errorMessage.value = "";
  return true;
};

// Handle form submission with validation
const handleSubmit = async () => {
  if (!allowEdit.value) return;

  if (!validateForm()) return; // Stop form submission if validation fails

  const formData = new FormData();
  loading.value = true;

  // Append user data fields to formData
  formData.append("lawyer", userData.value.lawyer);
  formData.append(
    "attonery_number__najiz",
    userData.value.attonery_number__najiz
  );
  formData.append("expiry_date", convertDate(userData.value.expiry_date));
  if (filetwo.value && filetwo.value.files.length > 0) {
    formData.append("file", filetwo.value.files[0]);
  }

  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.create_power_of_attorny.create_power_of_attorny",
      {
        method: "POST",
        body: formData,
      }
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
  } catch (error) {
    console.error("Error updating user data:", error);
  } finally {
    toggleDisable();
    loading.value = false;
    changeIcon.value = false;
  }
};

async function getAttorney() {
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_power_of_attorny.get_power_of_attorny"
    );
    const data = await response.json();
    if (data.message.response == "There are no power of attornies") {
      errorMessage.value = t("No Authorizations");
    } else {
      userData.value = data.message.response[0];
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    loading.value = false;
  }
}
const subscriptionStat = ref(false);
async function subscriptionStatus() {
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.get_subscription_status"
    );
    const data = await response.json();
    if (data.message.data.subscription) {
      subscriptionStat.value = true;
    } else {
      subscriptionStat.value = false;
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  } finally {
    loading.value = false;
  }
}

function copyClip(event) {
  const textToCopy = event.target.innerText;

  navigator.clipboard
    .writeText(textToCopy)
    .then(() => {
      showToastMessage(t("Copied to clipboard"), toastMessage, showToast);
    })
    .catch((err) => {
      showToastMessage(
        t("An unexpected error occurred. Please try again later."),
        toastMessage,
        showToast
      );
    });
}

onMounted(() => {
  getAttorney();
  subscriptionStatus();
});
</script>
