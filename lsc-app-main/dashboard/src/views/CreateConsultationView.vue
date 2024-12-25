<template>
  <LoggedInTopNav :title="servTitle" :backArrow="true" />

  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="w-full h-screen flex items-center justify-center p-8 bg-gray-100 my-24"
  >
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <form @submit.prevent="handleSubmit" class="space-y-4">
        <label class="form-control w-full text-black">
          {{ $t("Consultation Title") }}
        </label>
        <input
          v-model="title"
          type="text"
          :placeholder="t('Consultation Title')"
          class="input input-bordered w-full"
        />

        <label
          v-if="!servName.includes('كتابية') && !servName.includes('Written')"
          class="form-control w-full text-black"
        >
          {{ $t("Select Time") }}
        </label>
        <div
          v-if="!servName.includes('كتابية') && !servName.includes('Written')"
          class="flex flex-col gap-2 w-full"
        >
          <VueDatePicker
            v-model="date"
            :enable-time-picker="false"
            :min-date="minDate"
            :max-date="maxDate"
            range-separator="-"
            prevent-min-max-navigation
            class="text-right"
            :placeholder="t('Select Time')"
            text-input
          />
          <ul id="timetable" class="grid w-full grid-cols-3 gap-2">
            <li v-for="(slot, index) in availSlots" :key="index">
              <input
                type="radio"
                :id="'slot-' + index"
                :value="slot"
                v-model="selectedSlot"
                class="hidden peer"
                name="timetable"
                :disabled="isUnavailable(slot.fromTime)"
              />
              <label
                :for="'slot-' + index"
                style="direction: ltr"
                :class="[
                  'inline-flex items-center justify-center w-full p-1 text-[14px] font-medium text-center  hover:text-white  border rounded-lg cursor-pointer text-black border-gray-700 peer-checked:border-primary hover:border-gray-600 peer-checked:text-white peer-checked:bg-primary peer-checked:text-white hover:bg-gray-600 bg-white',
                  isUnavailable(slot.fromTime)
                    ? 'line-through !bg-red-800 hover:!bg-red-800 hover:!text-black'
                    : '',
                ]"
              >
                {{ formatTime(slot.fromTime) }}
              </label>
            </li>
          </ul>
        </div>
        <div
          v-if="message"
          class="mt-4 p-4 bg-green-100 text-green-800 border border-green-300 rounded"
          :class="messageClass"
        >
          {{ message }}
        </div>
        <label class="form-control w-full text-black">
          {{ $t("Description") }}
        </label>
        <textarea
          v-model="case_description"
          class="textarea textarea-bordered bg-white h-24 w-full"
          :placeholder="t('Description')"
        ></textarea>

        <div class="flex items-center justify-center w-full bg-white">
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
        </div>

        <button
          type="submit"
          class="btn btn-primary text-white border-white bg-primary w-full"
        >
          {{ $t("Send") }}
        </button>
      </form>
    </div>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import { ref, computed, watch } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { addDays } from "date-fns";
const router = useRouter();

const minDate = computed(() => new Date());
const maxDate = computed(() => addDays(new Date(), 15));
const upFile = ref(null);
const changeIcon = ref(false);
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    changeIcon.value = true; // Change icon once file is selected
    upFile.value = file.name;
  }
};
const date = ref("");
const loading = ref(false);
const case_description = ref("");
const title = ref("");
const file = ref(null);
const message = ref("");
const messageClass = ref("");
const route = useRoute();
const servName = route.query.elemnt || "";
const servTitle = route.query.elementName || "";
const availSlots = ref([]);
const unAvailSlots = ref([]);
const selectedSlot = ref(null);
const formatTime = (time) => {
  const [hours, minutes] = time.split(":");
  const date = new Date();
  date.setHours(hours, minutes);

  // Convert to 12-hour format
  const options = { hour: "numeric", minute: "numeric", hour12: true };
  return date.toLocaleString("en-US", options);
};

const convertDate = (date) => {
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, "0"); // Get the day and pad it with 0 if needed
  const month = String(d.getMonth() + 1).padStart(2, "0"); // Get the month (getMonth is 0-indexed) and pad with 0
  const year = String(d.getFullYear()).slice(-2); // Get last 2 digits of the year
  return `${year}-${month}-${day}`;
};

const handleSubmit = () => {
  if (title.value.length < 5) {
    message.value = t(
      "Name is required and must be at least 5 characters long."
    );
    messageClass.value = "bg-red-100 text-red-800 border border-red-300";
    return;
  }
  if (case_description.value.length < 5) {
    message.value = t(
      "Details are required and must be at least 5 characters long."
    );
    messageClass.value = "bg-red-100 text-red-800 border border-red-300";
    return;
  }
  if (!servName.includes("كتابية") && !servName.includes("Written")) {
    if (!selectedSlot.value) {
      message.value = t("Date is required");
      messageClass.value = "bg-red-100 text-red-800 border border-red-300";
      return;
    }
  }
  loading.value = true;
  const formData = new FormData();
  formData.append("consultation_name", servName);
  formData.append("title", title.value);
  if (selectedSlot.value) {
    formData.append("date", convertDate(date.value));
    formData.append("start_time", selectedSlot.value.fromTime);
    formData.append("end_time", selectedSlot.value.toTime);
  }
  formData.append("description", case_description.value);
  if (file.value && file.value.files.length > 0) {
    formData.append("file", file.value.files[0]);
  }

  axios
    .post(
      "/api/method/lsc_api.lsc_api.create_consultation.create_consultation",
      formData
    )
    .then((response) => {
      loading.value = false;
      const data = response.data;
      if (data.message.status === "جديد" || data.message.status === "New") {
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
watch(date, async (newDate) => {
  loading.value = true;
  if (newDate) {
    try {
      const response = await axios.post(
        "/api/method/lsc_api.lsc_api.doctype.employee_appointment.employee_appointment.get_availability_data",
        {
          date: newDate,
          item: servName,
        }
      );
      loading.value = false;
      message.value = "";

      availSlots.value = response.data.message.slot_details[0].avail_slot.map(
        (slot) => {
          return {
            fromTime: slot.from_time,
            toTime: slot.to_time,
          };
        }
      );
      unAvailSlots.value =
        response.data.message.slot_details[0].appointments.map(
          (appointment) => appointment.appointment_time
        );
    } catch (error) {
      loading.value = false;
      if (error.response.data.exception.includes("holiday")) {
        message.value = t("This is a Holiday, Select another day please");
        messageClass.value = "bg-red-100 text-red-800 border border-red-300";
        availSlots.value = [];
        unAvailSlots.value = [];
      } else if (error.response.data.exception.includes("No employees")) {
        message.value = t("No Available Employes in this Day");
        messageClass.value = "bg-red-100 text-red-800 border border-red-300";
        availSlots.value = [];
        unAvailSlots.value = [];
      } else {
        message.value = t(
          "An error occurred while selecting the day, try again"
        );
        messageClass.value = "bg-red-100 text-red-800 border border-red-300";
        availSlots.value = [];
        unAvailSlots.value = [];
      }
    }
  } else {
    loading.value = false;
  }
});

function convertTimeToTodayDate(timeString) {
  const [hours, minutes, seconds] = timeString.split(":").map(Number);
  const today = new Date();
  today.setHours(hours, minutes, seconds, 0);
  return today;
}

function isUnavailable(fromTime) {
  const currentTime = new Date();
  if (date?.value?.getDate() == currentTime.getDate()) {
    return (
      unAvailSlots.value.includes(fromTime) ||
      convertTimeToTodayDate(fromTime) < currentTime
    );
  } else {
    return unAvailSlots.value.includes(fromTime);
  }
}
</script>

<style scoped>
input {
  background-color: white;
}
</style>
