<template>
  <LoggedInTopNav :title="servTitle" :backArrow="true" />

  <div
    class="w-full h-screen flex items-center justify-center p-8 bg-gray-100"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <label class="form-control w-full">
          <input
            v-model="title"
            type="text"
            :placeholder="t('Case Title')"
            class="input input-bordered w-full"
          />
        </label>

        <label class="form-control w-full">
          <input
            v-model="description"
            type="text"
            :placeholder="t('Case Description')"
            class="input input-bordered w-full"
          />
        </label>

        <label
          for="dropzone-file"
          class="flex flex-col items-center justify-center h-full w-full h-16 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600 bg-white"
        >
          <div class="flex flex-col items-center justify-center pt-2 pb-2">
            <font-awesome-icon
              v-if="!changeIcon"
              icon="fa-solid fa-cloud-arrow-up"
            />
            <font-awesome-icon v-else icon="fa-solid fa-circle-check" />
            <span class="font-semibold">
              {{ changeIcon ? $t("File Attached") : $t("Attach File") }}
            </span>
            <p class="text-xs text-gray-500 dark:text-gray-400 truncate">
              {{ changeIcon ? upFile : $t("Images, Pdfs or Sounds") }}
            </p>
          </div>
          <input
            @change="handleFileChange"
            ref="file"
            id="dropzone-file"
            type="file"
            class="hidden"
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
const router = useRouter();

const loading = ref(false);
const title = ref("");
const description = ref("");
const file = ref(null);
const upFile = ref(null);
const changeIcon = ref(false);
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    changeIcon.value = true; // Change icon once file is selected
    upFile.value = file.name;
  }
};
const message = ref("");
const messageClass = ref("");
const route = useRoute();
const servName = route.query.elemnt || "";
const servTitle = route.query.elementName || "";

const handleSubmit = () => {
  // Validation: Check if the title is empty or less than 5 characters
  if (title.value.length < 5) {
    message.value = t("Please enter title (at least 5 characters)");
    messageClass.value = "bg-red-100 text-red-800 border border-red-300";
    return; // Stop the form submission if validation fails
  }
  loading.value = true;

  const formData = new FormData();
  formData.append("name", servName);
  formData.append("title", title.value);
  formData.append("case_description", description.value);
  if (file.value && file.value.files.length > 0) {
    formData.append("file", file.value.files[0]);
  }

  axios
    .post("/api/method/lsc_api.lsc_api.create_case.create_case", formData)
    .then((response) => {
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
</style>
