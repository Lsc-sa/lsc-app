<template>
  <LoggedInTopNav :title="t('Registration')" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="flex items-center justify-center min-h-screen px-6 sm:px-20 py-40 bg-gray-100"
  >
    <div class="w-full max-w-lg p-6 bg-white rounded-lg shadow-md">
      <div class="img max-w-20 mx-auto">
        <img :src="Logo" alt="LSC Logo" class="block w-full" />
      </div>
      <h2 class="mb-4 text-2xl font-bold text-center text-gray-700">
        {{ $t("Create Account") }}
      </h2>
      <form @submit.prevent="handleSubmit" class="text-right w-full h-auto">
        <!-- Branch select -->
        <div v-if="!form.branch" class="mb-4">
          <label
            for="firstname"
            class="block mb-2 text-sm font-medium text-gray-600"
          >
            {{ $t("Select the city to benefit from services") }}
          </label>
          <select
            v-model="form.branch"
            class="h-full w-full rounded-md border-2 bg-transparent py-0 pl-2 pr-7 text-gray-500 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm"
            style="direction: ltr"
          >
            <option
              v-for="branch in branchs"
              :key="branch"
              :value="branch.name"
            >
              {{ branch.branch_name }}
            </option>
          </select>
        </div>

        <!-- mobile_no Input -->
        <div v-if="form.branch && !waitCode" class="mb-4 countrycode">
          <label
            for="mobile_no"
            class="block mb-2 text-sm font-medium text-gray-600"
          >
            {{ $t("Phone Number") }}
          </label>
          <div class="relative mt-2 rounded-md shadow-sm w-full">
            <input
              type="tel"
              id="mobile_no"
              v-model="form.mobile_no"
              class="input input-sm input-bordered w-full text-black"
              placeholder="512345678"
              maxlength="9"
            />
          </div>
          <p v-if="errors.mobile_no" class="text-red-500 text-xs mt-2">
            {{ errors.mobile_no }}
          </p>
          <div v-if="form.branch">
            <button
              @click="() => checkNumber(form.mobile_no)"
              type="button"
              class="btn btn-primary text-white border-white bg-primary text-white w-full mt-4"
            >
              {{ $t("Send Code") }}
            </button>
          </div>
        </div>

        <!-- Code Checker Input -->
        <div
          v-if="form.branch && sendCodeCheck && waitCode && !correctCode"
          class="mb-4"
        >
          <label
            for="optCheck"
            class="block mb-2 text-sm font-medium text-gray-600"
          >
            {{ $t("Check Code") }}
            <!-- XXXXXX -->
          </label>
          <div class="relative mt-2 rounded-md shadow-sm w-full">
            <input
              type="tel"
              id="optCheck"
              v-model="otp"
              class="input input-sm input-bordered w-full text-black"
              placeholder="XXXXXX"
            />
          </div>
          <div>
            <button
              @click="() => checkOtp(form.mobile_no, String(otp))"
              type="button"
              class="btn btn-primary text-white border-white bg-primary text-white w-full mt-4"
            >
              {{ $t("Check Code") }}
            </button>
          </div>
        </div>

        <div v-if="form.branch && sendCodeCheck && correctCode">
          <!-- Full Name Input -->
          <div class="mb-4">
            <label
              for="firstname"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("First Name") }}
            </label>
            <input
              type="text"
              id="firstname"
              v-model="form.first_name"
              class="input input-sm input-bordered w-full text-black"
              :placeholder="t('First Name')"
            />
            <p v-if="errors.first_name" class="text-red-500 text-xs mt-2">
              {{ errors.first_name }}
            </p>
          </div>

          <!-- National ID Input -->
          <div class="mb-4">
            <label
              for="national_id"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("ID Number") }}
            </label>
            <input
              type="text"
              id="national_id"
              v-model="form.national_id"
              class="input input-sm input-bordered w-full text-black"
              :placeholder="t('Enter ID Number')"
            />
            <p v-if="errors.national_id" class="text-red-500 text-xs mt-2">
              {{ errors.national_id }}
            </p>
          </div>

          <!-- Password Input -->
          <div class="mb-4">
            <label
              for="password"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("Password") }}
            </label>
            <input
              type="password"
              id="password"
              v-model="form.password"
              class="input input-sm input-bordered w-full text-black"
              :placeholder="t('Enter Password')"
            />
            <p v-if="errors.password" class="text-red-500 text-xs mt-2">
              {{ errors.password }}
            </p>
          </div>

          <!-- rePassword Input -->
          <div class="mb-4">
            <label
              for="repassword"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("Re Enter Password") }}
            </label>
            <input
              type="password"
              id="repassword"
              v-model="form.repassword"
              class="input input-sm input-bordered w-full text-black"
              :placeholder="t('Re Enter Password')"
            />
            <p v-if="errors.repassword" class="text-red-500 text-xs mt-2">
              {{ errors.repassword }}
            </p>
          </div>

          <!-- Email Input -->
          <div class="mb-4">
            <label
              for="email"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("Enter Your Email") }}
            </label>
            <input
              type="email"
              id="email"
              v-model="form.email"
              class="input input-sm input-bordered w-full text-black"
              :placeholder="t('Enter Your Email')"
            />
            <p v-if="errors.email" class="text-red-500 text-xs mt-2">
              {{ errors.email }}
            </p>
          </div>
        </div>

        <!-- General Error -->
        <p v-if="errors.general" class="text-red-500 text-center text-xs mt-2">
          {{ errors.general }}
        </p>

        <!-- Signup Button -->
        <div v-if="form.branch && sendCodeCheck && correctCode">
          <button
            type="submit"
            class="btn btn-primary text-white border-white bg-primary text-white w-full"
          >
            {{ $t("Create Account") }}
          </button>
        </div>
      </form>

      <!-- Additional Links -->
      <div class="mt-6 text-center flex flex-col justify-center gap-2">
        <!-- href="https://portal.lsc-sa.net/" -->
        <a
          v-if="!form.branch"
          href="#"
          class="text-sm text-blue-600 hover:underline"
        >
          {{ $t("Can't find your city? Register to receive branch updates.") }}
        </a>

        <RouterLink to="/" class="text-sm text-blue-600 hover:underline">
          {{ $t("Login?") }}
        </RouterLink>
      </div>
    </div>
  </div>
  <!-- Toast Notification -->
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
  <!-- Loading? -->
  <Loader v-if="loading" />

  <!-- END LOADING -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import Loader from "@/components/Loader.vue";
import { ref, onMounted, watch } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import Logo from "../assets/images/icons/logo.png";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import showToastMessage from "../router/toastmessage";

const navigate = useRouter();

const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};
// Check loggedin
fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
  .then((response) => {
    if (!response.ok) {
      throw new Error("You are Not Logged In");
    }
    return response.json();
  })
  .then(() => navigate.replace("/home"))
  .catch((error) => {});

onMounted(() => {
  if (localStorage.getItem("language")) {
    locale.value = localStorage.getItem("language");
  } else {
    locale.value = "ar";
  }
  getBranchs();
});
// Toast Message
const toastMessage = ref(null);
const showToast = ref(false);
const loading = ref(false);
const waitCode = ref(false);
const sendCodeCheck = ref(false);
const correctCode = ref(false);
const repassword = ref("");

async function checkNumber(oldphone) {
  loading.value = true;
  const saudimobile_noRegex = /^5\d{8}$/;
  if (!saudimobile_noRegex.test(form.value.mobile_no)) {
    errors.value.mobile_no = t("Please enter a valid Saudi phone number.");
    sendCodeCheck.value = false;
  } else {
    let phone = `966${oldphone}`;
    loading.value = true;
    const response = await axios.get(
      "/api/method/lsc_api.lsc_api.forget_password.verify_mobile",
      { params: { mobile_no: phone } }
    );
    loading.value = false;
    if (response.data.message.status == "success") {
      showToastMessage(
        t("Phone Number is used before"),
        toastMessage,
        showToast
      );
    } else {
      sendCode(phone);
      sendCodeCheck.value = true;
    }
  }
  loading.value = false;
}

async function sendCode(phone) {
  // mobile_no validation for Saudi Arabia numbers
  loading.value = true;
  const response = await axios.post(
    "/api/method/lsc_api.lsc_api.sms_api.sms_api",
    { phone_number: phone, sms_type: "create_account" },
    {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    }
  );
  loading.value = false;
  if (response.data.message.status == "success") {
    sendCodeCheck.value = true;
    waitCode.value = true;
  } else {
    showToastMessage(
      t("Please enter a valid phone number."),
      toastMessage,
      showToast
    );
    waitCode.value = false;
  }
  loading.value = false;
}

const otp = ref("");
async function checkOtp(oldphone, num) {
  let phone = `966${oldphone}`;
  if (num.length != 6) {
    showToastMessage(t("Please write the 6 numbers"), toastMessage, showToast);
    return;
  }
  loading.value = true;
  const response = await axios.post(
    "/api/method/lsc_api.lsc_api.sms_api.validateOTP",
    { otp: num, phone_number: phone },
    {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    }
  );
  loading.value = false;
  if (response.data.message.status == "success") {
    correctCode.value = true;
  } else {
    showToastMessage(t("Code is incorrect."), toastMessage, showToast);
  }
  loading.value = false;
}

const branchs = ref([]);
async function getBranchs() {
  try {
    const response = await fetch(
      `/api/method/lsc_api.lsc_api.get_linked_data.get_branches?lang=${
        locale.value || "ar"
      }`
    );
    const data = await response.json();
    branchs.value = data?.message?.branches;
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
}
// Form fields
const form = ref({
  branch: "",
  first_name: "",
  password: "",
  repassword: "",
  email: "",
  mobile_no: "",
  national_id: "",
  username: "",
});

// Error state for form fields
const errors = ref({
  first_name: "",
  password: "",
  repassword: "",
  email: "",
  mobile_no: "",
  national_id: "",
  general: "",
});

watch(
  () => form.value.national_id,
  (newValue) => {
    form.value.username = newValue; // Update username whenever national_id changes
  }
);
const router = useRouter();

// Utility function to validate form inputs
const validateForm = () => {
  let isValid = true;
  // Clear previous errors
  Object.keys(errors.value).forEach((key) => {
    errors.value[key] = "";
  });

  // All fields are required
  for (const [key, value] of Object.entries(form.value)) {
    if (!value.trim()) {
      errors.value[key] = t("This field is required.");
      isValid = false;
    }
  }

  // Password validation
  const passwordRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(form.value.password)) {
    errors.value.password = t(
      "Password must be at least 8 characters long and include uppercase and lowercase letters, numbers, and symbols."
    );
    isValid = false;
  }

  if (form.value.password !== form.value.repassword) {
    errors.value.repassword = t("Passwords isn't matching.");
    isValid = false;
  }
  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(form.value.email)) {
    errors.value.email = t("Please enter a valid email.");
    isValid = false;
  }

  // mobile_no validation for Egyptian and Saudi Arabia numbers
  const saudimobile_noRegex = /^(9665\d{8}|5\d{8})$/;
  if (!saudimobile_noRegex.test(form.value.mobile_no)) {
    errors.value.mobile_no = t("Please enter a valid Saudi phone number.");
    isValid = false;
  }

  // National ID validation (assuming it follows a similar pattern as the mobile_no)
  const saudiNationalIdRegex = /^(1|2)\d{9}$/;
  if (!saudiNationalIdRegex.test(form.value.national_id)) {
    errors.value.national_id = t("Please enter a valid Saudi ID number.");
    isValid = false;
  }

  return isValid;
};

// Handle registration form submission
const handleSubmit = async () => {
  if (!validateForm()) {
    return;
  }
  loading.value = true;

  try {
    if (!form.value.mobile_no.startsWith("966")) {
      form.value.mobile_no = `966${form.value.mobile_no}`;
    }
    const response = await axios.post(
      "/api/method/lsc_api.lsc_api.register.register",
      { data: form.value },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    );
    loading.value = false;
    if (response.data.message.status === "success") {
      showToastMessage(t("Registered Successfully!"), toastMessage, showToast);
      setTimeout(() => {
        router.replace("/");
      }, 500);
    } else {
      errors.value.general = "Registration failed. Please try again.";
    }
  } catch (error) {
    loading.value = false;
    if (error.response) {
      // Handle specific error from the server
      if (error.response.data.message.message.includes("mobile_no")) {
        showToastMessage(
          t("The number is already in use, please choose a different number."),
          toastMessage,
          showToast
        );
        errors.value.mobile_no = t(
          "The number is already in use, please choose a different number."
        );
      } else if (error.response.data.message.message.includes("email")) {
        errors.value.email = t(
          "The email is already in use, please choose a different email."
        );
        showToastMessage(
          t("The email is already in use, please choose a different email."),
          toastMessage,
          showToast
        );
      } else if (error.response.data.message.message.includes("username")) {
        errors.value.email = t("ID Number Already Exist");
        showToastMessage(
          t("The ID is already in use, please choose a different ID."),
          toastMessage,
          showToast
        );
      } else {
        errors.value.general = t(
          "An unexpected error occurred. Please try again later."
        );
      }
    } else {
      // Handle network or other errors
      showToastMessage(
        t("Network error, please check your internet connection."),
        toastMessage,
        showToast
      );
    }
  }
};
</script>

<style scoped>
input {
  background: #f0f0f0;
}
.countrycode {
  position: relative;
  width: 100%;
  direction: ltr;
}

.countrycode input {
  width: 100%;
  padding-inline-start: 70px; /* Adjust padding as needed */
}

.countrycode::after {
  content: "+966 ";
  position: absolute;
  top: 24%;
  left: 10px;
  color: black;
}
</style>
