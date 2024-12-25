<template>
  <LoggedInTopNav :title="servTitle" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="w-full h-screen flex items-center justify-center p-8 bg-gray-100"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <label class="form-control w-full">
          <input
            v-model="title"
            type="text"
            :placeholder="t('Name')"
            class="input input-bordered w-full"
          />
          <p v-if="errors.title" class="text-red-600 text-sm">
            {{ errors.title }}
          </p>
        </label>

        <label class="form-control w-full">
          <textarea
            v-model="case_description"
            class="textarea textarea-bordered bg-white h-24 w-full"
            :placeholder="t('Details')"
          ></textarea>
          <p v-if="errors.case_description" class="text-red-600 text-sm">
            {{ errors.case_description }}
          </p>
        </label>

        <label class="form-control w-full">
          <div class="label">
            <span class="label-text-alt">
              {{ $t("Attach File") }}
            </span>
          </div>
          <input
            ref="file"
            type="file"
            class="file-input file-input-bordered file-input-sm w-full max-w-xs"
          />
        </label>

        <button
          type="submit"
          class="btn btn-primary text-white border-white bg-primary w-full"
        >
          {{ $t("Send") }}
        </button>
      </form>

      <div
        v-if="message"
        class="mt-4 p-4 bg-green-100 text-green-800 border border-green-300 rounded"
        :class="messageClass"
      >
        {{ message }}
      </div>
    </div>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import { ref } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";

const loading = ref(false);
const case_description = ref("");
const title = ref("");
const file = ref(null);
const message = ref("");
const messageClass = ref("");
const errors = ref({});
const route = useRoute();
const router = useRouter();
const servName = route.query.elemnt || "";
const servTitle = route.query.elementName || "";

// Validate form input
const validateForm = () => {
  errors.value = {};
  if (!title.value || title.value.length < 5) {
    errors.value.title = t(
      "Name is required and must be at least 5 characters long."
    );
  }
  if (!case_description.value || case_description.value.length < 5) {
    errors.value.case_description = t(
      "Details are required and must be at least 5 characters long."
    );
  }
  return Object.keys(errors.value).length === 0;
};

const handleSubmit = () => {
  if (!validateForm()) {
    return;
  }

  loading.value = true;
  const formData = new FormData();
  formData.append("name", servName);
  formData.append("title", title.value);
  formData.append("description", case_description.value);
  if (file.value && file.value.files.length > 0) {
    formData.append("file", file.value.files[0]);
  }

  axios
    .post(
      "/api/method/lsc_api.lsc_api.create_case_study.create_case_study",
      formData
    )
    .then((response) => {
      loading.value = false;
      const data = response.data;
      if (data.message.status === "success") {
        message.value = t("Successfully Booked");
        messageClass.value =
          "bg-green-100 text-green-800 border border-green-300";
        setTimeout(() => {
          router.push({
            path: `/requests/requestDetails/`,
            query: { requestId: data.message.client_transaction },
          });
        }, 500);
      } else {
        message.value = t("An error occurred while booking");
        messageClass.value = "bg-red-100 text-red-800 border border-red-300";
      }
    })
    .catch((error) => {
      loading.value = false;
      messageClass.value = "bg-red-100 text-red-800 border border-red-300";
      if (error.response.data.exception.includes("hours")) {
        message.value = t("Remaining hour balance is insufficient.");
        setTimeout(() => {
          router.push({
            path: `/packages`,
            query: { requestId: data.message.client_transaction },
          });
        }, 1500);
      } else if (error.response.data.exception.includes("expire_date")) {
        message.value = t(
          "The attached authorization is invalid, please check the authorization date."
        );
      } else {
        message.value = t("An error occurred while booking the service");
      }
    });
};
</script>

<style scoped>
input {
  background-color: white;
}
.text-red-600 {
  color: #dc2626;
}
</style>
