<template>
  <section
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="packages w-full px-4 min-h-screen lg:min-h-80 xl:min-h-screen flex flex-col justify-center items-center"
    id="packages"
  >
    <SectionTitle :title="t('Packages')" />
    <div
      class="pricing-cards flex flex-col place-content-center lg:flex-row gap-4 lg:flex-wrap"
    >
      <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.SafeLife.title") }}
        </h3>
        <h2 class="price text-6xl font-light">
          {{ $t("PackagesSection.SafeLife.price") }}
        </h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.SafeLife.duration") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.SafeLife.targetAudience") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.SafeLife.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.SafeLife.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.SafeLife.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.SafeLife.consultationHours") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.SafeLife.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.SafeLife.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.SafeLife.Cas") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.SafeLife.cases") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div>
      <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.General.name") }}
        </h3>
        <h2 class="price text-6xl font-light">-</h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.General.membership_type") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.General.target_category") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.General.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.General.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.General.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.General.consultations") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.General.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.General.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.General.Cas") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.General.cases") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div>
      <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.Relaxed.name") }}
        </h3>
        <h2 class="price text-6xl font-light">-</h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.Relaxed.membership_type") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.Relaxed.target_category") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.Relaxed.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.Relaxed.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.Relaxed.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.Relaxed.consultations") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.Relaxed.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.Relaxed.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.Relaxed.Cas") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.Relaxed.cases") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div>
      <!-- <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.safetyA.name") }}
        </h3>
        <h2 class="price text-6xl font-light">-</h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.safetyA.membership_type") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.safetyA.target_category") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyA.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyA.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyA.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyA.consultations") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyA.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyA.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyA.labCase") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyA.labor_issues") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyA.civCriCase") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyA.civil_or_criminal_case") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div>
      <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.safetyB.name") }}
        </h3>
        <h2 class="price text-6xl font-light">-</h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.safetyB.membership_type") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.safetyB.target_category") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyB.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyB.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyB.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyB.consultations") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyB.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyB.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyB.labCase") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyB.labor_issues") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div>
      <div
        class="pricing-card max-w-80 lg:min-w-80 flex flex-col justify-between gap-4 px-16 py-8 items-center bg-white rounded-md mt-8 hover:scale-105 duration-500"
      >
        <h3 class="text-2xl font-bold -mb-4">
          {{ $t("PackagesSection.safetyC.name") }}
        </h3>
        <h2 class="price text-6xl font-light">-</h2>
        <p class="font-semibold text-2xl -mt-4">
          {{ $t("PackagesSection.safetyC.membership_type") }}
        </p>
        <p class="text-sm text-center font-black">
          {{ $t("PackagesSection.safetyC.target_category") }}
        </p>
        <div class="price-notes flex flex-col gap-2 w-full text-center">
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyC.lang") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyC.languages") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyC.cons") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyC.consultations") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
          <p>
            {{ $t("PackagesSection.safetyC.supp") }}
            <span class="text-primary text-lg font-bold me-2">
              {{ $t("PackagesSection.safetyC.support_and_assistance") }}
            </span>
          </p>
          <hr class="bg-white w-full" />
        </div>
        <div
          class="pri-btns flex flex-col gap-4 items-center justify-center w-full"
        >
          <a
            class="text-white font-bold py-2 px-4 rounded w-full btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            href="https://portal.lsc-sa.net/dashboard"
          >
            {{ $t("Subscribe") }}
          </a>
          <button
            class="text-white font-bold py-2 px-4 rounded w-1/2 btn bg-primary border-primary hover:bg-emerald-600 hover:border-emerald-600"
            onclick="my_modal_2.showModal()"
          >
            {{ $t("Early Register") }}
          </button>
        </div>
      </div> -->
    </div>
  </section>
</template>

<style scoped>
.price {
  position: relative;
}
.price::before {
  /* content: "SAR"; */
  content: "";
  font-weight: 700;
  font-size: 16px;
  position: absolute;
  top: 0;
  left: -25%;
}
</style>

<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>
