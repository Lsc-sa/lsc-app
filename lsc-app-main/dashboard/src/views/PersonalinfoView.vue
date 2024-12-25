<template>
  <LoggedInTopNav :title="t('Personal Information')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="flex flex-col sm:flex-row w-full px-6 gap-5 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="card article bg-white rounded-box flex-grow px-4 py-10 gap-10 shadow-md"
    >
      <!-- Form Start -->
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
        <div class="flex flex-col gap-4">
          <div class="flex gap-4 justify-evenly items-center overflow-x-scroll">
            <div
              class="imgone relative"
              @click="allowEdit ? triggerFileone() : null"
            >
              <img
                :src="userData.custom_customer_ssn_photo_back || id_face"
                alt="ProfilePic"
                class="w-1/2 max-w-60 w-full block rounded-2 max-h-52"
              />
              <div
                v-if="allowEdit"
                class="absolute top-0 left-0 w-full h-full bg-white bg-opacity-75 flex items-center justify-center cursor-pointer"
              >
                <font-awesome-icon
                  icon="fa-solid fa-camera"
                  class="text-black"
                />
              </div>

              <!-- Hidden File Input -->
              <input
                type="file"
                ref="fileone"
                accept="image/*"
                class="hidden"
                @change="handleFileChangeback"
              />
            </div>
            <div
              class="imgtwo relative"
              @click="allowEdit ? triggerFiletwo() : null"
            >
              <img
                :src="userData.custom_customer_ssn_photo || id_face"
                alt="ProfilePic"
                class="w-1/2 max-w-60 w-full block rounded-2 max-h-52"
              />
              <div
                v-if="allowEdit"
                class="absolute top-0 left-0 w-full h-full bg-gray-800 bg-opacity-75 flex items-center justify-center cursor-pointer"
              >
                <font-awesome-icon
                  icon="fa-solid fa-camera"
                  class="text-black"
                />
              </div>

              <!-- Hidden File Input -->
              <input
                type="file"
                ref="filetwo"
                accept="image/*"
                class="hidden"
                @change="handleFileChangeface"
              />
            </div>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">{{ $t("Name") }}</span>
              </div>
              <input
                type="text"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.full_name"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Nationality") }}
                </span>
              </div>
              <select
                class="select select-bordered w-full select-sm bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                id="job"
                :disabled="!allowEdit"
                v-model="userData.custom_nationality"
              >
                <option :value="userData.custom_nationality">
                  {{ userData.custom_nationality }}
                </option>
                <option v-for="country in countries" :value="country.name">
                  {{ country.country_name }}
                </option>
              </select>
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("ID Number") }}
                </span>
              </div>
              <input
                type="text"
                maxlength="14"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.custom_id_number"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Sponsor Name") }}
                </span>
              </div>
              <input
                type="text"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.custom_kafeel_name"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Date of Birth") }}
                </span>
              </div>
              <VueDatePicker
                v-model="userData.birth_date"
                :enable-time-picker="false"
                range-separator="-"
                prevent-min-max-navigation
                :max-date="maxDate"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Date of Entry to Saudi Arabia") }}
                </span>
              </div>
              <VueDatePicker
                :enable-time-picker="false"
                :max-date="maxDate"
                range-separator="-"
                prevent-min-max-navigation
                v-model="userData.custom_ksa_entering_date"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Passport Number") }}
                </span>
              </div>
              <input
                type="tel"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.custom_passport_number"
                :disabled="!allowEdit"
              />
            </label>
          </div>

          <div class="flex flex-col md:flex-row gap-4">
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("National Address") }}
                </span>
              </div>
              <input
                type="text"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.location"
                :disabled="!allowEdit"
              />
            </label>
          </div>
        </div>

        <!-- Buttons for Save and Edit -->
        <button
          class="btn btn-success text-white w-full max-w-40 self-center"
          type="submit"
          :class="allowEdit ? '' : ' hidden'"
        >
          {{ $t("Save Changes") }}
        </button>
      </form>
      <button
        class="btn btn-primary text-white border-white bg-primary text-white w-full max-w-40 self-center"
        @click.prevent="toggleDisable"
        :class="allowEdit ? 'bg-danger' : ''"
      >
        {{ allowEdit ? $t("Undo") : $t("Edit") }}
      </button>
      <!-- Form End -->
    </div>
  </div>
  <Loader v-if="loading" />
  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import { ref, onMounted } from "vue";
import id_face from "@/assets/images/id_front.png";
import { useRouter } from "vue-router";
const countries = ref([]);
const loading = ref(false);
const maxDate = new Date();

const convertDate = (date) => {
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, "0");
  const month = String(d.getMonth() + 1).padStart(2, "0");
  const year = String(d.getFullYear()).slice(-2);
  return `${year}-${month}-${day}`;
};

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
  birth_date: "",
  location: "",
  custom_id_number: "",
  custom_passport_number: "",
  custom_nationality: "",
  custom_kafeel_name: "",
  custom_ksa_entering_date: "",
  custom_customer_ssn_photo_back: "",
  custom_customer_ssn_photo: "",
});

const allowEdit = ref(false);

// Fetch user data when component is mounted
const getUserData = async () => {
  loading.value = true;
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_user_data.get_user_data"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    loading.value = false;
    const data = await response.json();
    userData.value = data.message.user_data;
  } catch (error) {
    loading.value = false;
    console.error("Error fetching user data:", error);
  }
};

const fileone = ref(null);
const filetwo = ref(null);

const triggerFileone = () => {
  fileone.value.click();
};
const triggerFiletwo = () => {
  filetwo.value.click();
};

// Handle form submission
const handleSubmit = async () => {
  if (!allowEdit.value) return;

  const formData = new FormData();
  loading.value = true;
  // Append user data fields to formData
  formData.append("full_name", userData.value.full_name);
  formData.append("birth_date", convertDate(userData.value.birth_date));
  formData.append("location", userData.value.location);
  formData.append("custom_id_number", userData.value.custom_id_number);
  formData.append(
    "custom_passport_number",
    userData.value.custom_passport_number
  );
  formData.append("custom_nationality", userData.value.custom_nationality);
  formData.append("custom_kafeel_name", userData.value.custom_kafeel_name);
  formData.append(
    "custom_ksa_entering_date",
    convertDate(userData.value.custom_ksa_entering_date)
  );
  if (fileone.value && fileone.value.files.length > 0) {
    formData.append("custom_customer_ssn_photo_back", fileone.value.files[0]);
  }
  if (filetwo.value && filetwo.value.files.length > 0) {
    formData.append("custom_customer_ssn_photo", filetwo.value.files[0]);
  }

  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.update_user_data.update_user_data",
      {
        method: "PATCH",
        body: formData, // Send the formData
      }
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
  } catch (error) {
    console.error("Error updating user data:", error);
  } finally {
    toggleDisable(); // Disable editing after saving
    loading.value = false;
  }
};

function toggleDisable() {
  allowEdit.value = !allowEdit.value;
  if (!allowEdit.value) getUserData();
}

const handleFileChangeback = (event) => {
  const file = event.target.files[0];
  if (file && file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = (e) => {
      userData.value.custom_customer_ssn_photo_back = e.target.result;
    };
    reader.readAsDataURL(file); // Store the file in userData for form submission
  }
};
const handleFileChangeface = (event) => {
  const file = event.target.files[0];
  if (file && file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = (e) => {
      userData.value.custom_customer_ssn_photo = e.target.result;
    };
    reader.readAsDataURL(file); // Store the file in userData for form submission
  }
};
function fetchCountries() {
  fetch(
    // `/api/method/lsc_api.lsc_api.get_linked_data.get_countries?lang=${
    //   locale.value || "en"
    // }`,
    // { method: "GET" }
    `/api/method/lsc_api.lsc_api.get_linked_data.get_countries?lang=${locale.value}`,
    { method: "GET" }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch countries.");
      }
      return response.json();
    })
    .then((data) => {
      countries.value = data.message.nationality;
    })
    .catch((error) => {
      console.error("Error fetching countries:", error);
    });
}

onMounted(() => {
  getUserData();
  fetchCountries();
});
</script>

<style scoped>
input {
  text-align: end;
}
.article {
  flex: 3;
}
.aside {
  flex: 0.5;
}

.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-img {
  border-radius: 50%;
}

li {
  font-size: 14px;
  line-height: 3;
  color: #8f8f8f;
}

li:first-child {
  color: black;
}

@media (max-width: 640px) {
  .article {
    flex: 1;
  }

  .aside {
    flex: 1;
  }

  .divider-horizontal {
    display: none;
  }

  .profile-img {
    width: 100px;
    height: 100px;
  }
}
</style>
