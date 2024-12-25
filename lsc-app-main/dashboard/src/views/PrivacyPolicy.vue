<template>
  <LoggedInTopNav :title="t('Privacy Policy')" :backArrow="true" />

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
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { ref, onMounted } from "vue";

const policies = ref("");
async function fetchPrivPoli() {
  // fetch privacy policy from server
  const response = await fetch(
    "/api/method/lsc_api.lsc_api.get_terms.get_terms?term_name=privacy_policy"
  );
  const data = await response.json();
  // return privacy policy
  policies.value = data.message.term_text;
}

onMounted(() => {
  fetchPrivPoli();
});

/*
  <div class="commented">
  <div
    v-if="$i18n.locale == 'ar'"
    class="prof flex flex-col w-full px-6 gap-8 mt-24 lg:mt-40 pb-24"
  >
    <div
      class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
    >
      <!-- Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        سياسة الخصوصية لمركز المساندة القانونية
      </h3>

      <!-- Section A: المقدمة -->
      <h4 class="text-xl font-semibold mt-4 mb-2">أ – المقدمة:</h4>
      <p class="mb-4">
        1. في مركز المساندة القانونية، يتم منح أهمية كبيرة لحماية خصوصية
        المستخدمين وضمان سرية وأمان المعلومات الشخصية التي يتم جمعها ومعالجتها
        من خلال التطبيق الخاص بنا. يتم الالتزام بتبني أفضل الممارسات لضمان حماية
        معلومات المستخدمين وعدم مشاركتها مع أي جهة خارجية دون موافقة صريحة.
      </p>
      <p class="mb-4">
        2. توضح سياسة الخصوصية هذه كيفية جمع المعلومات الشخصية واستخدامها
        وحمايتها أثناء استخدام خدماتنا الرقمية. بموافقتك على هذه السياسة عند
        استخدام تطبيقنا أو موقعنا الإلكتروني، فإنك تقر بموافقتك على جمع واستخدام
        والكشف عن بياناتك الشخصية وفقًا لما هو موضح أدناه. وفي حال عدم موافقتك
        على بنود هذه السياسة، يرجى عدم تزويدنا بمعلوماتك الشخصية.
      </p>

      <!-- Section B: حقوق الملكية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">ب – حقوق الملكية:</h4>
      <p class="mb-4">
        1. يتم حماية جميع حقوق التأليف والنشر والعلامات التجارية المتعلقة
        بالمحتوى المقدم من قبل مركز المساندة القانونية وشريكها الاستراتيجي "شركة
        تكامل للخدمات القانونية". يمنع نسخ أو إعادة إنتاج أي محتوى دون الحصول
        على إذن مسبق.
      </p>

      <!-- Section C: جمع المعلومات الشخصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        ج – جمع المعلومات الشخصية:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          المعلومات التي يتم جمعها تشمل تفاصيل الأجهزة المستخدمة (مثل عنوان IP،
          والموقع الجغرافي، ونوع المتصفح).
        </li>
        <li>معلومات حول زيارات المستخدمين لموقعنا أو التطبيق.</li>
        <li>
          المعلومات التي تدخل عند التسجيل أو إنشاء حساب، مثل البريد الإلكتروني.
        </li>
        <li>المعلومات المتعلقة بالخدمات المستخدمة عبر التطبيق أو الموقع.</li>
      </ul>

      <!-- Section D: استخدام المعلومات الشخصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        د – استخدام المعلومات الشخصية:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>يتم استخدام المعلومات لإدارة التطبيق والخدمات.</li>
        <li>تخصيص تجربة المستخدم لتلبية احتياجاته.</li>
        <li>إرسال الفواتير والإشعارات، وإدارة المعاملات.</li>
        <li>حماية التطبيق من الاحتيال وتعزيز الأمان.</li>
      </ul>

      <!-- Section E: الكشف عن المعلومات الشخصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        هـ – الكشف عن المعلومات الشخصية:
      </h4>
      <p class="mb-4">
        1. يمكن الكشف عن معلوماتك لأي من موظفينا أو شركائنا بالقدر اللازم لتحقيق
        أغراض الخدمة.
      </p>
      <p class="mb-4">
        2. سيتم الكشف عن المعلومات إذا كان ذلك مطلوبًا بموجب القانون.
      </p>

      <!-- Section F: النقل الدولي للبيانات -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        و – النقل الدولي للبيانات:
      </h4>
      <p class="mb-4">
        1. قد يتم نقل معلوماتك الشخصية إلى دول أخرى لأغراض المعالجة، وفقًا
        للقوانين المحلية والدولية.
      </p>

      <!-- Section G: الاحتفاظ بالمعلومات الشخصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        ز – الاحتفاظ بالمعلومات الشخصية:
      </h4>
      <p class="mb-4">
        1. يتم الاحتفاظ بالمعلومات الشخصية طالما كان ذلك ضروريًا للأغراض التي
        جمعت من أجلها أو حسبما يتطلب القانون.
      </p>

      <!-- Section H: أمن المعلومات الشخصية -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        ح – أمن المعلومات الشخصية:
      </h4>
      <p class="mb-4">
        1. يتم اتخاذ جميع التدابير التقنية والتنظيمية لحماية معلوماتك الشخصية من
        الضياع أو إساءة الاستخدام.
      </p>

      <!-- Section I: التعديلات -->
      <h4 class="text-xl font-semibold mt-4 mb-2">ط – التعديلات:</h4>
      <p class="mb-4">
        1. يحتفظ المركز بالحق في تعديل سياسة الخصوصية في أي وقت. سيتم إعلام
        المستخدمين بأي تغييرات تطرأ عليها.
      </p>

      <!-- Section J: حقوقك -->
      <h4 class="text-xl font-semibold mt-4 mb-2">ي – حقوقك:</h4>
      <p class="mb-4">
        1. يحق لك طلب الوصول إلى المعلومات الشخصية التي نحتفظ بها عنك وتحديثها
        أو تصحيحها.
      </p>

      <!-- Section K: ملفات تعريف الارتباط -->
      <h4 class="text-xl font-semibold mt-4 mb-2">م – ملفات تعريف الارتباط:</h4>
      <p class="mb-4">
        1. قد يتم استخدام ملفات تعريف الارتباط لتخصيص وتحسين تجربة المستخدم.
      </p>

      <!-- Section L: حذف الحساب -->
      <h4 class="text-xl font-semibold mt-4 mb-2">ن – حذف الحساب:</h4>
      <p class="mb-4">1. يمكن طلب حذف الحساب من داخل التطبيق.</p>
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
      <!-- Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        Privacy Policy of the Legal Aid Center
      </h3>

      <!-- Section A: Introduction -->
      <h4 class="text-xl font-semibold mt-4 mb-2">A – Introduction:</h4>
      <p class="mb-4">
        1. At the Legal Aid Center, great importance is given to protecting the
        privacy of users and ensuring the confidentiality and security of
        personal information collected and processed through our application. We
        are committed to adopting best practices to ensure the protection of
        user information and not sharing it with any third party without
        explicit consent.
      </p>
      <p class="mb-4">
        2. This privacy policy outlines how personal information is collected,
        used, and protected while using our digital services. By agreeing to
        this policy when using our application or website, you acknowledge your
        consent to the collection, use, and disclosure of your personal data as
        described below. If you do not agree to the terms of this policy, please
        do not provide us with your personal information.
      </p>

      <!-- Section B: Ownership Rights -->
      <h4 class="text-xl font-semibold mt-4 mb-2">B – Ownership Rights:</h4>
      <p class="mb-4">
        1. All copyright and trademark rights related to the content provided by
        the Legal Aid Center and its strategic partner, "Takamul Legal Services
        Company," are protected. Copying or reproducing any content without
        prior permission is prohibited.
      </p>

      <!-- Section C: Collection of Personal Information -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        C – Collection of Personal Information:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          The information collected includes details of the devices used (such
          as IP address, geographic location, and browser type).
        </li>
        <li>Information about users' visits to our website or application.</li>
        <li>
          Information entered during registration or account creation, such as
          email address.
        </li>
        <li>
          Information related to services used through the application or
          website.
        </li>
      </ul>

      <!-- Section D: Use of Personal Information -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        D – Use of Personal Information:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>The information is used to manage the application and services.</li>
        <li>Personalizing the user experience to meet their needs.</li>
        <li>Sending invoices and notifications, and managing transactions.</li>
        <li>Protecting the application from fraud and enhancing security.</li>
      </ul>

      <!-- Section E: Disclosure of Personal Information -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        E – Disclosure of Personal Information:
      </h4>
      <p class="mb-4">
        1. Your information may be disclosed to any of our employees or partners
        as necessary to achieve service purposes.
      </p>
      <p class="mb-4">2. Information will be disclosed if required by law.</p>

      <!-- Section F: International Data Transfer -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        F – International Data Transfer:
      </h4>
      <p class="mb-4">
        1. Your personal information may be transferred to other countries for
        processing, in accordance with local and international laws.
      </p>

      <!-- Section G: Retention of Personal Information -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        G – Retention of Personal Information:
      </h4>
      <p class="mb-4">
        1. Personal information is retained as long as necessary for the
        purposes for which it was collected or as required by law.
      </p>

      <!-- Section H: Security of Personal Information -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        H – Security of Personal Information:
      </h4>
      <p class="mb-4">
        1. All technical and organizational measures are taken to protect your
        personal information from loss or misuse.
      </p>

      <!-- Section I: Amendments -->
      <h4 class="text-xl font-semibold mt-4 mb-2">I – Amendments:</h4>
      <p class="mb-4">
        1. The center reserves the right to amend the privacy policy at any
        time. Users will be informed of any changes made to it.
      </p>

      <!-- Section J: Your Rights -->
      <h4 class="text-xl font-semibold mt-4 mb-2">J – Your Rights:</h4>
      <p class="mb-4">
        1. You have the right to request access to the personal information we
        hold about you and to update or correct it.
      </p>

      <!-- Section K: Cookies -->
      <h4 class="text-xl font-semibold mt-4 mb-2">K – Cookies:</h4>
      <p class="mb-4">
        1. Cookies may be used to customize and improve the user experience.
      </p>

      <!-- Section L: Account Deletion -->
      <h4 class="text-xl font-semibold mt-4 mb-2">L – Account Deletion:</h4>
      <p class="mb-4">
        1. Account deletion can be requested from within the application.
      </p>
    </div>
  </div>
</div>
*/
</script>
