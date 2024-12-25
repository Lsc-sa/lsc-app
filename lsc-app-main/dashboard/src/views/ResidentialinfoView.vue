<template>
  <LoggedInTopNav :title="t('Residence Information')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="flex flex-col sm:flex-row w-full px-6 gap-5 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="card article bg-white rounded-box flex-grow px-4 py-10 gap-10 shadow-md"
    >
      <!-- Form to handle data submission -->
      <form @submit.prevent="handleSubmit" class="flex flex-col gap-6">
        <div class="flex flex-col gap-4">
          <h2 class="font-bold text-lg">
            {{ $t("Residence Information") }}
          </h2>
          <!-- Image Display and Upload -->
          <div
            class="relative flex justify-center"
            @click="allowEdit ? triggerFileInputIqama() : null"
          >
            <img
              class="max-w-full h-full object-cover max-h-52"
              :src="userData.custom_iqama_image || id_face"
              alt="Iqama Image"
            />
            <!-- Overlay with Camera Icon -->
            <div
              v-if="allowEdit"
              class="absolute top-0 left-0 w-full h-full bg-white bg-opacity-75 flex items-center justify-center cursor-pointer"
            >
              <font-awesome-icon icon="fa-solid fa-camera" class="text-black" />
            </div>
            <!-- Hidden File Input -->
            <input
              type="file"
              ref="fileInputIqama"
              accept="image/*"
              class="hidden"
              @change="handleFileChangeIqama"
            />
          </div>
          <div class="flex flex-col md:flex-row gap-4">
            <!-- Input Fields -->
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Sponsor's Residence") }}
                </span>
              </div>
              <input
                type="text"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.custom_kafeel_address"
                :disabled="!allowEdit"
              />
            </label>
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("City of Work") }}
                </span>
              </div>
              <select
                class="select select-bordered w-full select-sm bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                id="job"
                :disabled="!allowEdit"
                v-model="userData.custom_work_city"
              >
                <option :value="userData.custom_work_city">
                  {{ userData.custom_work_city }}
                </option>
                <option
                  v-for="territory in territories"
                  :value="territory.name"
                >
                  {{ territory.territory_name }}
                </option>
              </select>
            </label>
            <label class="form-control flex-1 font-bold">
              <div class="label">
                <span class="label-text">
                  {{ $t("Salary") }}
                </span>
              </div>
              <input
                type="tel"
                class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
                v-model="userData.custom_salary"
                :disabled="!allowEdit"
              />
            </label>
          </div>
          <!-- The button to open modal for job contract-->
          <label
            for="my_modal_7"
            class="btn btn-primary text-white border-white bg-primary text-white"
          >
            {{ $t("View Employment Contract") }}
          </label>

          <!-- Put this part before </body> tag -->
          <input type="checkbox" id="my_modal_7" class="modal-toggle" />
          <div class="modal" role="dialog">
            <div class="modal-box flex flex-col gap-2 justify-center">
              <h3 class="text-lg font-bold text-center">
                {{ $t("Employment Contract") }}
              </h3>
              <div
                class="relative"
                @click="allowEdit ? triggerFileInput() : null"
              >
                <embed
                  class="w-full min-h-80 h-full object-cover"
                  :src="userData.custom_job_contract || id_face"
                  alt="Job Contract"
                />
                <!-- Overlay with Camera Icon -->
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
                  ref="fileInput"
                  accept="image/*,.pdf,.doc,.docx"
                  class="hidden"
                  @change="handleFileChange"
                />
              </div>
              <!-- <a
                class="btn btn-ghost btn-xs"
                :href="userData.custom_job_contract"
                download
                >تحميل</a
              > -->
            </div>
            <label class="modal-backdrop" for="my_modal_7"> </label>
          </div>
        </div>
        <!-- Save and Edit buttons -->
        <button
          class="btn btn-success text-white w-full max-w-40 self-center"
          type="submit"
          :class="allowEdit ? '' : ' hidden'"
        >
          {{ $t("Save Changes") }}
        </button>
        <button
          class="btn btn-primary text-white border-white bg-primary text-white w-full max-w-40 self-center"
          @click.prevent="toggleDisable"
          :class="allowEdit ? 'bg-danger' : ''"
        >
          {{ allowEdit ? $t("Undo") : $t("Edit") }}
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

import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import id_face from "@/assets/images/id_front.png";

const loading = ref(false);
const navigate = useRouter();
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};

const fileInput = ref(null);
const triggerFileInput = () => {
  fileInput.value.click();
};
const fileInputIqama = ref(null);
const triggerFileInputIqama = () => {
  fileInputIqama.value.click();
};

const userData = ref({
  custom_kafeel_address: "",
  custom_salary: 0.0,
  custom_work_city: "",
  custom_job_contract: "",
  custom_iqama_image: "",
});

const allowEdit = ref(false);

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

const toggleDisable = () => {
  allowEdit.value = !allowEdit.value;
  if (!allowEdit.value) getUserData();
};

// Handle file change and store the file in userData
const handleFileChange = (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    userData.value.custom_job_contract = e.target.result;
  };
  reader.readAsDataURL(file);
};
// Handle file change and store the file in userData
const handleFileChangeIqama = (event) => {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = (e) => {
    userData.value.custom_iqama_image = e.target.result;
  };
  reader.readAsDataURL(file);
};

const territories = ref([]);

function fetchTerritories() {
  fetch(
    `/api/method/lsc_api.lsc_api.get_linked_data.get_work_cities?lang=${locale.value}`,
    { method: "GET" }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch territories.");
      }
      return response.json();
    })
    .then((data) => {
      territories.value = data.message.work_city;
    })
    .catch((error) => {
      console.error("Error fetching territories:", error);
    });
}
// Handle form submission
const handleSubmit = async () => {
  loading.value = true;
  const formData = new FormData();
  formData.append(
    "custom_kafeel_address",
    userData.value.custom_kafeel_address
  );
  formData.append("custom_salary", userData.value.custom_salary);
  formData.append("custom_work_city", userData.value.custom_work_city);
  if (fileInput.value && fileInput.value.files.length > 0) {
    formData.append("custom_job_contract", fileInput.value.files[0]);
  }
  if (fileInputIqama.value && fileInputIqama.value.files.length > 0) {
    formData.append("custom_iqama_image", fileInputIqama.value.files[0]);
  }

  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.update_user_data.update_user_data",
      {
        method: "PATCH",
        body: formData, // Use FormData for PATCH request
      }
    );
    const data = await response.json();
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
  } catch (error) {
    loading.value = false;
    console.error("Error updating user data:", error);
  } finally {
    loading.value = false;
    toggleDisable();
  }
};

onMounted(() => {
  getUserData();
  fetchTerritories();
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
