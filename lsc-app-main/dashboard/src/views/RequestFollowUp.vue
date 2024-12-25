<template>
  <LoggedInTopNav title="التفاصيل" :backArrow="true" />

  <div class="w-full h-screen flex items-center justify-center p-8 bg-gray-100">
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <div v-if="caseData" class="space-y-4">
        <label class="form-control w-full">
          <input
            v-model="caseData.name"
            type="text"
            placeholder="الاسم"
            class="input input-bordered w-full"
            readonly
          />
        </label>

        <label class="form-control w-full">
          <input
            v-model="caseData.case_description"
            type="text"
            placeholder="التفاصيل"
            class="input input-bordered w-full"
            readonly
          />
        </label>

        <label class="form-control w-full">
          <div class="label">
            <span class="label-text-alt">الملف</span>
          </div>
          <input
            type="text"
            :value="caseData.file ? caseData.file.name : 'لا يوجد ملف'"
            class="input input-bordered w-full"
            readonly
          />
        </label>
      </div>
      <div v-else class="space-y-4">
        <label class="form-control w-full">
          <input
            type="text"
            value="الاسم غير متوفر"
            class="input input-bordered w-full"
            readonly
          />
        </label>

        <label class="form-control w-full">
          <input
            type="text"
            value="التفاصيل غير متوفرة"
            class="input input-bordered w-full"
            readonly
          />
        </label>

        <label class="form-control w-full">
          <input
            type="text"
            value="لا يوجد ملف"
            class="input input-bordered w-full"
            readonly
          />
        </label>
      </div>
    </div>
  </div>

  <!-- <BottomNav /> -->
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();

import { ref, onMounted } from "vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
// import BottomNav from "@/components/BottomNav.vue";
import { useRoute } from "vue-router";

const route = useRoute();
const caseData = ref(null);

// onMounted(() => {
//   const requestId = route.params.id;
//     console.log(requestId)
//   fetch(`/api/method/lsc_api.lsc_api.get_request_data/${requestId}`)
//     .then(response => response.json())
//     .then(data => {
//       caseData.value = data;
//     })
//     .catch(error => {
//       console.error('Error fetching request data:', error);
//     });
// });
</script>

<style scoped>
input {
  background-color: white;
}
</style>
