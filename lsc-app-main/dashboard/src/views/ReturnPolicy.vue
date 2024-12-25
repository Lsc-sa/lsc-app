<template>
  <LoggedInTopNav :title="t('Return Policy')" :backArrow="true" />

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
    "/api/method/lsc_api.lsc_api.get_terms.get_terms?term_name=return_policy"
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
      <!-- Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        سياسة الاستبدال والإرجاع
      </h3>

      <!-- Section 1: نطاق السياسة -->
      <h4 class="text-xl font-semibold mt-4 mb-2">1. نطاق السياسة:</h4>
      <p class="mb-4">
        تنطبق هذه السياسة على جميع الخدمات القانونية المقدمة عبر الموقع بنظام
        الباقات السنوية. يتوجب على العملاء قراءة هذه السياسة قبل الاشتراك في أي
        من خدماتنا.
      </p>

      <!-- Section 2: الإلغاء والاسترجاع -->
      <h4 class="text-xl font-semibold mt-4 mb-2">2. الإلغاء والاسترجاع:</h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          يمكن للعميل طلب إلغاء الاشتراك في الباقة السنوية خلال فترة 7 أيام من
          تاريخ الدفع الأولي، شرط عدم الاستفادة من أي من الخدمات القانونية
          المقدمة ضمن الباقة.
        </li>
        <li>
          في حالة طلب الإلغاء خلال فترة السماح، سيتم رد المبلغ المدفوع بالكامل
          بعد خصم أي رسوم إدارية أو مصرفية.
        </li>
        <li>
          إذا تم تقديم أي من الخدمات القانونية خلال فترة الإلغاء، لا يحق للعميل
          المطالبة برد المبلغ كاملاً، ويتم خصم قيمة الخدمات التي تم تقديمها
          بناءً على السعر المنفصل لكل خدمة.
        </li>
      </ul>

      <!-- Section 3: الاستبدال -->
      <h4 class="text-xl font-semibold mt-4 mb-2">3. الاستبدال:</h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          يمكن للعميل طلب استبدال الباقة بخدمة أخرى أو ترقية/تخفيض الباقة خلال
          أول 30 يومًا من الاشتراك، على أن يتم تسوية الفروق المالية بين الباقات.
        </li>
        <li>
          في حالة استبدال الباقة، يتم حساب أي فروقات مالية، ويُطلب من العميل دفع
          الفارق (في حال الترقية)، أو استرداد الفارق (في حال التخفيض).
        </li>
      </ul>

      <!-- Section 4: الخدمات غير القابلة للاسترجاع -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        4. الخدمات غير القابلة للاسترجاع:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          أي خدمات قانونية يتم تقديمها بشكل فوري مثل الاستشارات، إعداد الوثائق
          القانونية، أو تقديم المذكرات، لا تكون قابلة للاسترجاع أو الاستبدال بعد
          تقديم الخدمة.
        </li>
        <li>باقات الاشتراك المنتهية لا تكون قابلة للاسترجاع أو التمديد.</li>
      </ul>

      <!-- Section 5: آلية طلب الإرجاع أو الاستبدال -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        5. آلية طلب الإرجاع أو الاستبدال:
      </h4>
      <p class="mb-4">
        يجب تقديم طلب الإرجاع أو الاستبدال عبر البريد الإلكتروني الرسمي أو من
        خلال حساب العميل في الموقع. يتعين على العميل توضيح سبب طلب الإرجاع أو
        الاستبدال مع تقديم ما يثبت عدم الاستفادة من الخدمات (إن أمكن).
      </p>

      <!-- Section 6: الوقت المستغرق لمعالجة الطلبات -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        6. الوقت المستغرق لمعالجة الطلبات:
      </h4>
      <p class="mb-4">
        يتم معالجة طلبات الإلغاء، الاسترجاع أو الاستبدال في غضون 10 أيام عمل من
        تاريخ استلام الطلب.
      </p>

      <!-- Section 7: استثناءات -->
      <h4 class="text-xl font-semibold mt-4 mb-2">7. استثناءات:</h4>
      <p class="mb-4">
        تحتفظ الشركة بالحق في رفض أي طلب استرجاع أو استبدال في حالة وجود سوء
        استخدام أو خرق لشروط الخدمة من قبل العميل.
      </p>

      <!-- Section 8: التعديلات على السياسة -->
      <h4 class="text-xl font-semibold mt-4 mb-2">8. التعديلات على السياسة:</h4>
      <p class="mb-4">
        تحتفظ الشركة بحق تعديل هذه السياسة في أي وقت، وسيتم إخطار العملاء بأي
        تغييرات جوهرية من خلال الموقع.
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
      <!-- Header -->
      <h3 class="text-lg font-bold text-center pb-2">
        Return and Exchange Policy
      </h3>

      <!-- Section 1: Scope of Policy -->
      <h4 class="text-xl font-semibold mt-4 mb-2">1. Scope of Policy:</h4>
      <p class="mb-4">
        This policy applies to all legal services provided through the website
        under annual subscription packages. Customers must read this policy
        before subscribing to any of our services.
      </p>

      <!-- Section 2: Cancellation and Refund -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        2. Cancellation and Refund:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          The customer can request to cancel the annual subscription within 7
          days from the date of the initial payment, provided no legal services
          have been utilized under the package.
        </li>
        <li>
          If cancellation is requested within the grace period, the full amount
          paid will be refunded after deducting any administrative or banking
          fees.
        </li>
        <li>
          If any legal services have been provided during the cancellation
          period, the customer is not entitled to a full refund, and the value
          of the services provided will be deducted based on the individual
          price for each service.
        </li>
      </ul>

      <!-- Section 3: Exchange -->
      <h4 class="text-xl font-semibold mt-4 mb-2">3. Exchange:</h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          The customer can request to exchange the package for another service
          or upgrade/downgrade the package within the first 30 days of
          subscription, with financial differences between packages to be
          settled.
        </li>
        <li>
          In the case of package exchange, any financial differences will be
          calculated, and the customer will be required to pay the difference
          (in case of an upgrade) or receive a refund of the difference (in case
          of a downgrade).
        </li>
      </ul>

      <!-- Section 4: Non-Refundable Services -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        4. Non-Refundable Services:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          Any legal services provided immediately, such as consultations, legal
          document preparation, or submissions, are non-refundable or
          exchangeable once the service has been provided.
        </li>
        <li>Expired subscription packages are non-refundable or extendable.</li>
      </ul>

      <!-- Section 5: Request Mechanism for Return or Exchange -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        5. Request Mechanism for Return or Exchange:
      </h4>
      <p class="mb-4">
        Requests for return or exchange must be submitted via official email or
        through the customer’s account on the website. The customer must clarify
        the reason for the return or exchange request and provide proof of
        non-utilization of services (if possible).
      </p>

      <!-- Section 6: Processing Time for Requests -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        6. Processing Time for Requests:
      </h4>
      <p class="mb-4">
        Requests for cancellation, refund, or exchange will be processed within
        10 working days from the date of receipt of the request.
      </p>

      <!-- Section 7: Exceptions -->
      <h4 class="text-xl font-semibold mt-4 mb-2">7. Exceptions:</h4>
      <p class="mb-4">
        The company reserves the right to refuse any return or exchange request
        in the case of misuse or breach of service terms by the customer.
      </p>

      <!-- Section 8: Amendments to the Policy -->
      <h4 class="text-xl font-semibold mt-4 mb-2">
        8. Amendments to the Policy:
      </h4>
      <p class="mb-4">
        The company reserves the right to amend this policy at any time, and
        customers will be notified of any significant changes through the
        website.
      </p>
    </div>
  </div>
*/
</script>
