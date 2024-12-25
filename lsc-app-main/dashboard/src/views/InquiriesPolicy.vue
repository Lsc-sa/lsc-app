<template>
  <LoggedInTopNav :title="t('Inquiries Policy')" :backArrow="true" />

  <div class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24">
    <div
      :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
      v-if="policies"
      class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      v-html="policies"
    ></div>
  </div>
  <!-- <BottomNav /> -->
</template>

<script setup>
// import BottomNav from "@/components/BottomNav.vue";
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { ref, onMounted } from "vue";

const policies = ref("");
async function fetchPrivPoli() {
  // fetch privacy policy from server
  const response = await fetch(
    "/api/method/lsc_api.lsc_api.get_terms.get_terms?term_name=inquiries_policy"
  );
  const data = await response.json();
  // return inq poli
  policies.value = data.message.term_text;
}

onMounted(() => {
  fetchPrivPoli();
});

/*
  <div
    v-if="$i18n.locale == 'ar'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
    >
      <!-- Arabic Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        سياسة الإجابة على الاستفسارات ومعالجة الشكاوى
      </h3>

      <!-- Arabic Introduction -->
      <p class="mb-4">
        تهدف هذه السياسة إلى تنظيم عملية التعامل مع استفسارات وشكاوى العملاء
        لضمان تقديم خدمة عالية الجودة والاستجابة الفعالة.
      </p>

      <!-- Section 1: استقبال الاستفسارات والشكاوى -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        استقبال الاستفسارات والشكاوى:
      </h4>
      <ul class="list-disc pl-5 mb-4">
        <li>يمكن تقديم الاستفسارات والشكاوى عبر:</li>
        <li>
          الموقع الإلكتروني:
          <p class="text-black">https://portal.lsc-sa.net/</p>
        </li>
        <li>
          البريد الإلكتروني:
          <a href="mailto:info@lsc-sa.net" class="text-blue-600"
            >info@lsc-sa.net</a
          >
        </li>
        <li>الهاتف المخصص لخدمة العملاء: 055-955-7313</li>
      </ul>

      <!-- Section 2: معالجة الشكاوى -->
      <h4 class="text-xl font-semibold mt-4 mb-2">معالجة الشكاوى:</h4>
      <ul class="list-disc pl-5 mb-4">
        <li>
          يتم التحقيق في الشكوى بواسطة الفريق المختص لضمان تحليلها بشكل عادل
          ومحايد.
        </li>
        <li>
          يتم التواصل مع العميل خلال فترة التحقيق لتزويده بتحديثات عن حالة
          الشكوى.
        </li>
        <li>يتم توفير حلول مناسبة لكل شكوى بناءً على نتائج التحقيق.</li>
      </ul>

      <!-- Section 3: مراقبة الجودة والتقييم -->
      <h4 class="text-xl font-semibold mt-4 mb-2">مراقبة الجودة والتقييم:</h4>
      <ul class="list-disc pl-5 mb-4">
        <li>
          يتم مراجعة الشكاوى والاستفسارات بانتظام لتحسين العمليات وتعزيز جودة
          الخدمة.
        </li>
        <li>
          يتم تقييم مستوى رضا العملاء بعد حل كل شكوى لضمان تحسين مستوى الخدمة في
          المستقبل.
        </li>
      </ul>

      <!-- Section 4: السرية والخصوصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">السرية والخصوصية:</h4>
      <p class="mb-4">
        يتم التعامل مع جميع الاستفسارات والشكاوى بسرية تامة، وتتعهد الشركة بعدم
        مشاركة معلومات المستهلكين مع أي طرف ثالث دون إذن مسبق.
      </p>

      <!-- Arabic Conclusion -->
      <p class="mb-4">
        هذه السياسة تهدف إلى تعزيز ثقة العملاء في الشركة وضمان الشفافية في
        التعامل مع استفساراتهم وشكاويهم.
      </p>
    </div>
  </div>

  <div
    v-else
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
    >
      <!-- English Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        Complaints and Inquiries Policy
      </h3>

      <!-- English Introduction -->
      <p class="mb-4">
        This policy aims to organize the handling of customer inquiries and
        complaints to ensure high-quality service and effective responses.
      </p>

      <!-- Section 1: Receiving Inquiries and Complaints -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        Receiving Inquiries and Complaints:
      </h4>
      <ul class="list-disc pl-5 mb-4">
        <li>Inquiries and complaints can be submitted via:</li>
        <li>
          Website:
          <p class="text-black">https://portal.lsc-sa.net</p>
        </li>
        <li>
          Email:
          <a href="mailto:info@lsc-sa.net" class="text-blue-600"
            >info@lsc-sa.net</a
          >
        </li>
        <li>Customer service phone: 055-955-7313</li>
      </ul>

      <!-- Section 2: Handling Complaints -->
      <h4 class="text-xl font-semibold mt-4 mb-2">Handling Complaints:</h4>
      <ul class="list-disc pl-5 mb-4">
        <li>
          The complaint is investigated by the specialized team to ensure fair
          and impartial analysis.
        </li>
        <li>
          The customer is contacted during the investigation period to provide
          updates on the status of the complaint.
        </li>
        <li>
          Suitable solutions are provided for each complaint based on the
          investigation results.
        </li>
      </ul>

      <!-- Section 3: Quality Monitoring and Evaluation -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        Quality Monitoring and Evaluation:
      </h4>
      <ul class="list-disc pl-5 mb-4">
        <li>
          Complaints and inquiries are reviewed regularly to improve processes
          and enhance service quality.
        </li>
        <li>
          Customer satisfaction levels are evaluated after resolving each
          complaint to ensure service improvement in the future.
        </li>
      </ul>

      <!-- Section 4: Confidentiality and Privacy -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        Confidentiality and Privacy:
      </h4>
      <p class="mb-4">
        All inquiries and complaints are handled with complete confidentiality,
        and the company is committed not to share consumer information with any
        third party without prior consent.
      </p>

      <!-- English Conclusion -->
      <p class="mb-4">
        This policy aims to enhance customer trust in the company and ensure
        transparency in dealing with their inquiries and complaints.
      </p>
    </div>
  </div>

*/
</script>
