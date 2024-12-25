<template>
  <LoggedInTopNav :title="t('Package Managment')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="pt-4 bg-[ghostwhite] flex flex-col gap-4"
  >
    <div
      v-if="subscription"
      class="services px-6 gap-5 mt-20 lg:mt-40 sm:mt-32 bg-white mx-8 py-4 rounded-3xl shadow-mycard"
    >
      <table class="text-black w-full">
        <tbody>
          <tr>
            <td class="text-md text-start w-1/3 mb-2">
              {{ $t("Current Package") }}
              :
            </td>
            <td class="mx-auto text-primary text-center">
              {{ subscription.subscription_plan }}
            </td>
          </tr>
          <tr>
            <td class="text-md text-start">
              {{ $t("Price") }}
              :
            </td>
            <td class="mx-auto text-primary text-center">
              {{ subscription.plan_fees }}
              {{ $t("SAR") }}
            </td>
          </tr>
          <tr>
            <td class="text-md text-start">
              {{ $t("Package Status") }}
              :
            </td>
            <td class="mx-auto text-primary text-center">
              {{ subscription.status }}
            </td>
          </tr>
          <tr>
            <td class="text-md text-start">
              {{ $t("Subscription Date") }}
              :
            </td>
            <td class="mx-auto text-primary text-center">
              {{ subscription.invoice_start_date }}
            </td>
          </tr>
          <tr>
            <td class="text-md text-start">
              {{ $t("Subscription End Date") }}
              :
            </td>
            <td class="mx-auto text-danger text-center">
              {{ subscription.invoice_end_date }}
            </td>
          </tr>
        </tbody>
      </table>
      <!-- <RouterLink
        :to="{ name: 'PackagesView' }"
        class="text-end block text-success"
      >
        {{ $t("Renew or Change Package") }}
        ⩥
      </RouterLink> -->
    </div>
    <!-- All Services -->
    <div
      v-if="allServices && subscription"
      class="flex flex-wrap mx-8 justify-center gap-2"
    >
      <div
        v-for="(serv, index) in allServices"
        :key="index"
        class="bg-white shadow-mycard p-4 text-center rounded-xl relative"
      >
        <font-awesome-icon
          v-if="
            !subscription?.allowed_services?.some(
              (el) => el == serv.service_name
            )
          "
          :icon="['fas', 'lock']"
          class="absolute top-0 left-0 font-sm"
        />
        <span class="text-black">
          {{ serv.service_name }}
        </span>
      </div>
    </div>
    <div
      v-if="subscription"
      class="services px-6 gap-5 bg-white mx-8 py-4 mb-8 rounded-3xl shadow-mycard"
    >
      <div
        style="width: 100%; height: 300px"
        class="overflow-hidden rounded-3xl"
      >
        <ag-charts :options="chartOptions"></ag-charts>
      </div>
      <div
        class="cont flex w-full justify-between items-center max-w-96 mx-auto"
      >
        <div
          class="flex flex-col items-center justify-center gap-2 text-center"
        >
          <div
            class="radial-progress text-center"
            :style="`--value: 
            ${(
              (subscription.remaining_consultation_hrs /
                subscription.consultation_hrs) *
              100
            ).toFixed(2)}
          `"
            role="progressbar"
          >
            {{ subscription.consultation_hrs }} /
            {{ subscription.remaining_consultation_hrs }}
          </div>
          <span class="text-lg font-bold text-black">
            {{ $t("Consultations") }}
          </span>
        </div>
        <div
          class="flex flex-col items-center justify-center gap-2 text-center"
        >
          <div
            class="radial-progress text-center"
            :style="`--value: 
          ${(
            (subscription.remaining_cases_hrs / subscription.cases_hrs) *
            100
          ).toFixed(2)}
        `"
            role="progressbar"
          >
            {{ subscription.cases_hrs }} /
            {{ subscription.remaining_cases_hrs }}
          </div>
          <span class="text-lg font-bold text-black"> {{ $t("Cases") }} </span>
        </div>
        <div
          class="flex flex-col items-center justify-center gap-2 text-center"
        >
          <div
            class="radial-progress text-center"
            :style="`--value: 
            ${(
              (subscription.remaining_legal_services_hrs /
                subscription.legal_services_hrs) *
              100
            ).toFixed(2)}
          `"
            role="progressbar"
          >
            {{ subscription.legal_services_hrs }} /
            {{ subscription.remaining_legal_services_hrs }}
          </div>
          <span class="text-lg font-bold text-black">
            {{ $t("Services") }}
          </span>
        </div>
      </div>
    </div>
    <div
      v-if="subscription"
      class="w-full flex items-center justify-center mb-8"
    >
      <label
        class="btn bg-danger border-danger text-white"
        onclick="my_modal_1.showModal()"
        @click="acceptRefund"
      >
        {{ $t("Refund your subscription") }}
      </label>
      <!-- Put this part before </body> tag -->
      <dialog class="modal" id="my_modal_1" role="dialog">
        <div class="modal-box text-center">
          <h3 class="text-lg font-bold">
            {{ $t("Are you sure you want to Refund your package?") }}
          </h3>
          <p class="py-4">
            {{ $t("You can contact customer service from here.") }}
          </p>
          <div class="btns-action">
            <!-- The button to open modal -->
            <label
              for="my_custom_modal"
              class="btn bg-danger text-white w-full max-w-40"
              onclick="my_custom_modal.showModal()"
              @click="acceptRefund2"
            >
              {{ $t("I want to Refund the Package.") }}
            </label>
            <!-- Put this part before </body> tag -->
            <dialog class="modal" id="my_custom_modal" role="dialog">
              <div class="modal-box text-center">
                <h3 class="text-lg font-bold">
                  {{ $t("You cannot revert this.") }}
                </h3>
                <p class="py-4">
                  {{ $t("You will lose your subscription") }}
                </p>
                <div class="btns-action">
                  <button
                    class="btn bg-danger"
                    type="button"
                    @click="handleRefund"
                  >
                    {{ $t("Confirm Refund") }}
                  </button>
                </div>
                <div class="modal-action">
                  <form method="dialog">
                    <!-- if there is a button in form, it will close the modal -->
                    <button ref="warnBTN" class="btn bg-success">
                      {{ $t("Undo") }}
                    </button>
                  </form>
                </div>
              </div>
            </dialog>
            <div class="modal-action">
              <form method="dialog">
                <button ref="warnBTN2" class="btn bg-success">
                  {{ $t("Undo") }}
                </button>
              </form>
            </div>
          </div>
        </div>
      </dialog>
    </div>

    <div
      v-else
      class="services w-full px-6 gap-5 flex flex-col items-center justify-center mt-20 lg:mt-40 sm:mt-32"
    >
      <h2 class="services__heading font-bold text-gray-400 mb-2 lg:text-5xl">
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
import BottomNav from "@/components/BottomNav.vue";
import Loader from "@/components/Loader.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { ref, onMounted, watch, onBeforeUnmount, inject, reactive } from "vue";
import { notificationsState } from "../router/notificationsState";
import { AgCharts } from "ag-charts-vue3";
import showToastMessage from "../router/toastmessage";

const remHours = ref("15");
const conHours = ref("20");
const chartOptions = ref({});
const loading = ref(false);
const navigate = useRouter();
const subscription = ref([]);
const router = useRouter();
const allServices = ref([]);
const showToast = ref(false);
const toastMessage = ref(null);
const firstWarn = ref(false);
const secondWarn = ref(false);
const warnBTN = ref(null);
const warnBTN2 = ref(null);

const triggerWarnButton = () => {
  if (warnBTN.value) {
    warnBTN.value.click();
  }
  if (warnBTN2.value) {
    warnBTN2.value.click();
  }
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

const fetchServices = async () => {
  loading.value = true;
  const response = await fetch(
    "/api/method/lsc_api.lsc_api.get_allowed_services.get_allowed_services"
  );
  const data = await response.json();
  allServices.value = data.message?.allowed_services?.sort((a, b) =>
    a.service_name.localeCompare(b.service_name, "ar")
  );
  loading.value = false;
};

const fetchData = async () => {
  loading.value = true;
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.get_subscription_status"
    );
    const data = await response.json();
    const val = data.message.data.subscription;
    if (val && val != "null") {
      loading.value = false;
      subscription.value = data.message.data.subscription;
      conHours.value = Math.abs(
        subscription.value.total_hours - subscription.value.remaining_hours
      );
      remHours.value = subscription.value.remaining_hours;
      chartOptions.value = {
        data: [
          {
            segment: t("Consumed"),
            value: parseInt(conHours.value),
          },
          {
            segment: t("Remaining"),
            value: parseInt(remHours.value),
          },
        ],
        title: {
          text: data.message.data.subscription.subscription_plan,
          fontFamily: "Cairo",
          fontWeight: "bold",
        },
        subtitle: {
          enabled: true,
          text: `${subscription?.value?.total_hours} ${t("Total Hours")}`,
          fontFamily: "Cairo",
        },
        legend: {
          pagination: {
            label: {
              fontFamily: "Cairo",
            },
          },
          item: {
            label: {
              fontFamily: "Cairo",
              fontWeight: "bold",
            },
          },
        },
        series: [
          {
            type: "pie",
            angleKey: "value",
            calloutLabelKey: "segment",
            sectorLabelKey: "value",
            fills: ["#981D20", "#5978B9"],
            sectorLabel: {
              color: "white",
              fontFamily: "Cairo",
              fontWeight: "bold",
            },
            tooltip: {
              enabled: false,
            },
          },
        ],
      };
    } else {
      loading.value = false;
      subscription.value = null;
    }
  } catch (error) {
    loading.value = false;
    console.error("Error fetching data:", error);
  }
};
function acceptRefund() {
  firstWarn.value = true;
}
function acceptRefund2() {
  secondWarn.value = true;
}

async function handleRefund() {
  triggerWarnButton();
  if (firstWarn && secondWarn) {
    loading.value = true;
    try {
      const response = await fetch(
        `/api/method/lsc_api.lsc_api.get_payment_status.refund`
      );
      const data = await response.json();
      if (data.message.status == "refunded") {
        showToastMessage(t("Package Refunded"), toastMessage, showToast);
        setTimeout(() => {
          router.go("/");
        }, 800);
      } else if (
        data.message.status == "fail" &&
        data.message.message.includes("consumed_hours")
      ) {
        showToastMessage(
          t("You can't refund once you consumed any of your hours"),
          toastMessage,
          showToast
        );
      } else if (
        data.message.status == "fail" &&
        data.message.message.includes("days_diff")
      ) {
        showToastMessage(
          t("You can't refund once you exceeded 15 days of subscriping"),
          toastMessage,
          showToast
        );
      } else {
        showToastMessage(
          t("An unexpected error occurred. Please try again later."),
          toastMessage,
          showToast
        );
      }
      // if (data.message.status == "paid") {
      //   messageStatus.value = true;
      // } else {
      //   messageStatus.value = false;
      // }
    } catch (error) {
      console.error("error" + error);
    } finally {
      loading.value = false;
    }
  } else {
    firstWarn.value = false;
    secondWarn.value = false;
  }
}
// const goToCaseStudyDetail = (requestId) => {
//   router.push({
//     path: `/requests/requestDetails`,
//     query: { requestId: requestId },
//   });
// };

onMounted(() => {
  fetchData();
  fetchServices();
});
</script>
