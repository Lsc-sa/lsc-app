<template>
  <LoggedInTopNav :title="t('Account Status')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="p-6 w-full px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
    >
      <div
        v-if="accStat?.status != 'fail'"
        class="layout flex flex-col items-center gap-4"
      >
        <div
          class="rd border-b-2 border-primary rounded-md px-2 py-2 flex w-full items-center justify-between"
        >
          <div class="flex gap-2 items-center">
            <div
              :class="[
                unsetFields?.user_status == 'Incomplete'
                  ? 'bg-red-400'
                  : 'bg-emerald-400',
              ]"
            >
              <p
                class="flex items-center justify-center w-6 h-6 rounded-full text-white"
              >
                1
              </p>
            </div>
            <div
              v-if="unsetFields?.user_status == 'Incomplete'"
              class="text flex flex-col items-start"
            >
              <RouterLink
                :to="{ name: 'NProfileView' }"
                v-if="attorneyData == 'Incomplete'"
                class="text-gray-400"
              >
                {{ $t("Complete Info") }}
              </RouterLink>
              <h2 class="text-primary font-bold">
                {{ $t("Complete your profile info") }}
              </h2>
              <p class="text-gray-400">
                {{ $t("Not Completed") }}:
                <span v-for="(item, index) in unsetFields.unset_user_labels">
                  {{ item }}
                  {{
                    index != unsetFields.unset_user_labels.length - 1
                      ? " - "
                      : ""
                  }}
                </span>
              </p>
            </div>
            <div v-else class="text flex flex-col items-start">
              <h2 class="text-primary font-bold">
                {{ $t("Your data is completed") }}
              </h2>
              <h2 class="text-gray-400">
                {{ $t("This step is completed") }}
              </h2>
            </div>
          </div>
          <img :src="task" width="24" height="24" alt="icon" />
        </div>
        <div
          class="rd border-b-2 border-primary rounded-md px-2 py-2 flex w-full items-center justify-between"
        >
          <div class="flex gap-2 items-center">
            <div
              :class="[
                contractData == 'Incomplete' ? 'bg-red-400' : 'bg-emerald-400',
              ]"
            >
              <p
                class="flex items-center justify-center w-6 h-6 rounded-full text-white"
              >
                2
              </p>
            </div>
            <div class="text flex flex-col items-start">
              <h2
                v-if="printLink && contractData == 'Complete'"
                class="text-primary font-bold"
              >
                {{ $t("Contract successfully signed") }}
              </h2>
              <h2
                v-else-if="printLink && subscriptionStatus != 'Inactive'"
                class="text-primary font-bold"
              >
                {{ $t("Please sign the following contract") }}
              </h2>
              <h2
                v-if="printLink && contractData == 'Complete'"
                class="text-gray-400"
              >
                {{ $t("This step is completed") }}
              </h2>
              <RouterLink
                v-if="printLink && contractData == 'Complete'"
                :to="{
                  path: '/profile/allInvoices/AnewPrint',
                  query: { invoice: printLink, height: heightQuery },
                }"
                target="_blank"
                class="text-primary text-center"
              >
                {{ $t("View the contract") }}
              </RouterLink>
              <h2
                v-if="unsetFields?.user_status == 'Incomplete'"
                class="text-gray-400"
              >
                {{ $t("Complete the previous step") }}
              </h2>
              <div
                v-else-if="
                  unsetFields?.user_status == 'Complete' &&
                  subscriptionStatus == 'Inactive' &&
                  contractData == 'Incomplete'
                "
                class="services w-full px-6 gap-5 flex flex-col items-center justify-center"
              >
                <h2
                  class="services__heading font-bold text-gray-400 mb-2 lg:text-5xl"
                >
                  {{ $t("No Subscription") }}
                </h2>
                <RouterLink :to="{ name: 'PackagesView' }">
                  <button
                    class="btn btn-primary text-white border-white bg-primary text-white lg:btn-lg"
                  >
                    {{ $t("Subscribe Now") }}
                  </button>
                </RouterLink>
              </div>
              <RouterLink
                v-if="
                  unsetFields?.user_status == 'Complete' &&
                  subscriptionStatus != 'Inactive' &&
                  contractData == 'Incomplete'
                "
                :to="{
                  path: '/profile/allInvoices/AnewPrint',
                  query: { invoice: printLink, height: heightQuery },
                }"
                target="_blank"
                class="text-primary text-center"
              >
                {{ $t("View the contract") }}
              </RouterLink>
              <div class="flex gap-2 items-center justify-center">
                <input
                  v-if="
                    unsetFields?.user_status == 'Complete' &&
                    subscriptionStatus != 'Inactive' &&
                    contractData == 'Incomplete'
                  "
                  name="check"
                  id="check"
                  :checked="isChecked"
                  @click="toggleCheck"
                  type="checkbox"
                  class="checkbox checkbox-sm"
                />
                <label
                  v-if="
                    unsetFields?.user_status == 'Complete' &&
                    subscriptionStatus != 'Inactive' &&
                    contractData == 'Incomplete'
                  "
                  for="check"
                  class="block text-sm font-medium text-primary"
                >
                  {{ $t("I Accept to Sign this Contract") }}
                </label>
              </div>
              <p
                v-if="
                  isChecked &&
                  unsetFields?.user_status == 'Complete' &&
                  subscriptionStatus != 'Inactive' &&
                  contractData == 'Incomplete'
                "
                class="text-gray-400 text-center"
              >
                {{ $t("Draw your signature below") }}
              </p>
            </div>
          </div>
          <img :src="edit" width="24" height="24" alt="icon" />
        </div>
        <div
          v-if="
            isChecked &&
            unsetFields?.user_status == 'Complete' &&
            subscriptionStatus != 'Inactive' &&
            contractData == 'Incomplete'
          "
          class="w-full p-2 flex flex-col gap-2"
        >
          <VueSignaturePad
            ref="signaturePad"
            height="300px"
            class="rounded-md w-full h-[300px] border-2 border-black"
            :options="{
              penColor: 'black',
              backgroundColor: 'rgb(242 242 242)',
            }"
          />
          <div class="btcl flex w-full justify-evenly items-center">
            <button
              class="border-primary rounded-sm text-black px-4 py-2"
              @click="clearSignature"
            >
              {{ $t("Clear") }}
            </button>
            <button
              class="border-danger rounded-sm text-black px-4 py-2"
              @click="saveSignature"
            >
              {{ $t("Save Signature") }}
            </button>
          </div>
          <input type="hidden" :value="signatureData" />
        </div>
        <div
          class="rd border-b-2 border-primary rounded-md px-2 py-2 flex w-full items-center justify-between"
        >
          <div class="flex gap-2 items-center">
            <div
              :class="[
                attorneyData == 'Incomplete' ? 'bg-red-400' : 'bg-emerald-400',
              ]"
            >
              <p
                class="flex items-center justify-center w-6 h-6 rounded-full text-white"
              >
                3
              </p>
            </div>
            <div class="text flex flex-col items-start">
              <RouterLink
                :to="{ name: 'PowerofAttView' }"
                v-if="attorneyData == 'Incomplete'"
                class="text-primary font-bold"
              >
                {{ $t("Attach power of attorney") }}
              </RouterLink>
              <h2 v-else class="text-primary font-bold">
                {{ $t("Power of attorney is attached") }}
              </h2>
              <h2 v-if="attorneyData == 'Complete'" class="text-gray-400">
                {{ $t("This step is completed") }}
              </h2>
              <!-- <h2 class="text-gray-400">
                {{ $t("Complete the previous step") }}
              </h2> -->
            </div>
          </div>
          <img :src="addnote" width="24" height="24" alt="icon" />
        </div>
        <RouterLink v-if="asp_status" @click.prevent="goBack" to="#">
          <div class="accomInfo flex justify-between items-center">
            <div class="rig flex gap-2 items-center text-primary">
              <p class="text-primary">
                {{ $t("Skip") }}
              </p>
            </div>
          </div>
        </RouterLink>
      </div>
      <div v-else class="layout flex flex-col items-center gap-4">
        <h1 class="text-primary font-bold">
          {{ $t("An unexpected error occurred. Please try again later.") }}
        </h1>
        <RouterLink :to="{ name: 'userhome' }">
          <div class="accomInfo flex justify-between items-center">
            <div class="rig flex gap-2 items-center text-primary">
              <p class="text-primary">
                {{ $t("Home") }}
              </p>
            </div>
          </div>
        </RouterLink>
      </div>
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
</template>
<script setup>
import { useI18n } from "vue-i18n";
import axios from "axios";
const { t, locale } = useI18n();
import { RouterLink, useRouter } from "vue-router";
import addnote from "../assets/images/icons/addnote.svg";
import edit from "../assets/images/icons/edit-2.svg";
import task from "../assets/images/icons/task.svg";
import { ref, onMounted } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import showToastMessage from "../router/toastmessage";

// import BottomNav from "@/components/BottomNav.vue";
import { VueSignaturePad } from "vue-signature-pad";
const loading = ref(true);

const signaturePad = ref(null); // Reference to the signature pad
const signatureData = ref(""); // Holds the base64 data of the signature
const printLink = ref("");
const heightQuery = ref("27cm");
const router = useRouter();
const showToast = ref(false);
const toastMessage = ref(null);
const asp_status = ref(true);
const isChecked = ref(false);
function toggleCheck() {
  isChecked.value = !isChecked.value;
}
const goBack = () => {
  localStorage.setItem("asp_status", 1);
  router.go(-1);
};
// Clears the signature pad
const clearSignature = () => {
  signaturePad.value.clearSignature();
};

fetch("/api/method/frappe.auth.get_logged_user", {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
})
  .then((response) => {
    if (!response.ok) {
      throw new Error("You are not logged In");
    }
    return response.json();
  })
  .then()
  .catch(() => navigate.replace("/"));

// Saves the signature as base64
const saveSignature = async () => {
  loading.value = true;
  signatureData.value = signaturePad.value.saveSignature();
  if (signaturePad.value.isEmpty()) {
    return;
  }
  const sign = signatureData.value.data;

  const formData = new FormData();
  formData.append("signature", sign);

  const response = await fetch(
    "/api/method/lsc_api.lsc_api.insert_signature.insert_signature",
    {
      method: "PATCH",
      body: formData, // Send the formData
    }
  );
  const data = await response.json();
  if (data.message.status == "fail") {
    if (data.message.message.includes("No unsigned")) {
      showToastMessage(
        t("No available Contract, Contact Support."),
        toastMessage,
        showToast
      );
      setTimeout(() => {
        router.push("/packages");
      }, 800);
    } else {
      showToastMessage(
        t("An unexpected error occurred. Please try again later."),
        toastMessage,
        showToast
      );
    }
  } else {
    printLink.value = data.message.print;
    heightQuery.value = data.message.height;
    getAccountStatus();
  }

  loading.value = false;
};

const accStat = ref(null);
const contractData = ref(null);
const attorneyData = ref(null);
const subscriptionStatus = ref(null);
const unsetFields = ref([]);

async function getAccountStatus() {
  try {
    const res = await axios.get(
      "/api/method/lsc_api.lsc_api.check_account_status.check_account_status",
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    );
    accStat.value = res.data.message;
    unsetFields.value = res.data.message.user_details;
    contractData.value = res.data.message.contract_details.contract_status;
    attorneyData.value = res.data.message.attorney_details.poa_status;
    subscriptionStatus.value = res.data.message.subscription_status;
    printLink.value = res.data.message.print;
    loading.value = false;
  } catch (error) {
    loading.value = false;
    console.error("Error creating payment:", error);
  }
}
onMounted(() => {
  getAccountStatus();
  if (localStorage.getItem("asp_status") == 2) {
    asp_status.value = false;
  }
});
</script>
