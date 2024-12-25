<template>
  <LoggedInTopNav :title="t('Reset Password')" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="flex px-6 sm:px-20 items-center justify-center min-h-screenpx-6 py-40 bg-gray-100 rtl"
  >
    <div class="w-full max-w-sm p-6 bg-white rounded-lg shadow-md">
      <div class="img max-w-20 mx-auto">
        <img :src="Logo" alt="LSC Logo" class="block w-full" />
      </div>
      <h2 class="mb-4 text-2xl font-bold text-center text-gray-700">
        {{ $t("Reset Password") }}
      </h2>
      <form @submit.prevent="handleReset" class="text-right">
        <!-- mobile_no Input -->
        <div v-if="!sendCodeCheck" class="mb-4 countrycode">
          <label
            for="mobile_no"
            class="block mb-2 text-sm font-medium text-gray-600"
          >
            {{ $t("Phone Number") }}
            <!-- 966 5458921 -->
          </label>
          <div class="relative mt-2 rounded-md shadow-sm w-full">
            <input
              type="tel"
              id="mobile_no"
              v-model="form.mobile_no"
              class="input input-sm input-bordered w-full text-black"
              placeholder="512345678"
            />
          </div>
          <p v-if="errors.mobile_no" class="text-red-500 text-xs mt-2">
            {{ errors.mobile_no }}
          </p>
          <div>
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
        <div v-if="sendCodeCheck && !correctCode" class="mb-4">
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
              maxlength="6"
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

        <div v-if="sendCodeCheck && correctCode">
          <!-- Password Input -->
          <div class="mb-4">
            <label
              for="password"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("Enter Password") }}
            </label>
            <input
              type="password"
              id="password"
              v-model="form.password"
              class="input input-bordered w-full text-black"
              :placeholder="t('Enter Password')"
              autocomplete="current-password"
            />
            <!-- Error Message for Password -->
            <p v-if="errors.password" class="text-red-500 text-xs mt-2">
              {{ errors.password }}
            </p>
          </div>
          <div class="mb-6">
            <label
              for="repassword"
              class="block mb-2 text-sm font-medium text-gray-600"
            >
              {{ $t("Re Enter Password") }}
            </label>
            <input
              type="password"
              id="repassword"
              v-model="repassword"
              class="input input-bordered w-full text-black"
              :placeholder="t('Re Enter Password')"
              autocomplete="current-password"
            />
            <!-- Error Message for Password -->
            <p v-if="errors.repassword" class="text-red-500 text-xs mt-2">
              {{ errors.repassword }}
            </p>
          </div>
        </div>

        <!-- General Error Message -->
        <p v-if="errors.general" class="text-red-500 text-center text-xs mt-2">
          {{ errors.general }}
        </p>

        <!-- Save Password Button -->
        <div v-if="sendCodeCheck && correctCode">
          <button
            type="submit"
            class="btn btn-primary text-white border-white bg-primary w-full text-white"
          >
            {{ $t("Save Password") }}
          </button>
        </div>
      </form>

      <!-- Additional Links -->
      <div class="mt-6 text-center">
        <RouterLink to="/" class="text-sm text-blue-600 hover:underline">
          {{ $t("Login") }}
        </RouterLink>
      </div>
      <div class="mt-2 text-center">
        <RouterLink to="/signup" class="text-sm text-blue-600 hover:underline">
          {{ $t("Don't have an account? Create Account") }}
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
  <div
    v-if="loading"
    class="loader absolute z-20 flex bg-gray-200 bg-opacity-40 justify-center items-center w-screen h-screen left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2"
  >
    <span class="loading text-primary loading-ring loading-lg"></span>
  </div>
  <!-- END LOADING -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import Logo from "../assets/images/icons/logo.png";
import axios from "axios";
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { RouterLink } from "vue-router";
import showToastMessage from "../router/toastmessage";

// Toast Message
const toastMessage = ref(null);
const showToast = ref(false);
const loading = ref(false);

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
      // error 403
      throw new Error("You are Not Logged In");
    }
    // no error,
    return response.json();
  })
  .then(() => navigate.replace("/home"))
  .catch((error) => {});

const sendCodeCheck = ref(false);
const correctCode = ref(false);
const repassword = ref("");

async function checkNumber(oldphone) {
  let phone = `966${oldphone}`;
  loading.value = true;
  const saudimobile_noRegex = /^5\d{8}$/;
  if (!saudimobile_noRegex.test(form.value.mobile_no)) {
    errors.value.mobile_no = t("Please enter a valid Saudi phone number.");
    sendCodeCheck.value = false;
  } else {
    loading.value = true;
    const response = await axios.get(
      "/api/method/lsc_api.lsc_api.forget_password.verify_mobile",
      { params: { mobile_no: phone } }
    );
    loading.value = false;
    if (response.data.message.status == "success") {
      sendCode(phone);
      sendCodeCheck.value = true;
    } else {
      showToastMessage(
        t("Please enter a valid phone number."),
        toastMessage,
        showToast
      );
    }
  }
  loading.value = false;
}

async function sendCode(phone) {
  // mobile_no validation for Saudi Arabia numbers
  loading.value = true;
  const response = await axios.post(
    "/api/method/lsc_api.lsc_api.sms_api.sms_api",
    { phone_number: phone, sms_type: "forget_password" },
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
  } else {
    showToastMessage(
      t("Please enter a valid phone number."),
      toastMessage,
      showToast
    );
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

// Form Data
const form = ref({
  password: "",
  mobile_no: "",
});

// Error state for form fields
const errors = ref({
  password: "",
  repassword: "",
  mobile_no: "",
  general: "",
});
const router = useRouter();

// Form Validation Function
const validateForm = () => {
  let isValid = true;
  const passwordRegex =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  if (!passwordRegex.test(form.value.password)) {
    errors.value.password = t(
      "Password must be at least 8 characters long and include uppercase and lowercase letters, numbers, and symbols."
    );
    isValid = false;
  }

  if (form.value.password !== repassword.value) {
    errors.value.repassword = t("Passwords isn't matching.");
    isValid = false;
  }
  errors.value.password = "";
  errors.value.repassword = "";
  return isValid;
};

// Handle Login
const handleReset = async () => {
  if (!validateForm()) return;
  form.value.mobile_no = `966${form.value.mobile_no}`;
  loading.value = true;
  try {
    const response = await axios.post(
      "/api/method/lsc_api.lsc_api.forget_password.reset_password",
      {
        mobile_no: form.value.mobile_no,
        new_password: form.value.password,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    );

    loading.value = false;
    showToastMessage(t("Password Changed"), toastMessage, showToast);
    setTimeout(() => {
      router.replace("/");
    }, 500);
  } catch {
    errors.value.general = "Failed. Please try again.";
    loading.value = false;
  } finally {
    loading.value = false;
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
