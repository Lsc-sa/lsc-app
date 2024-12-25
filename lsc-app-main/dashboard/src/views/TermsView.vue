<template>
  <LoggedInTopNav :title="t('Terms of Use')" :backArrow="true" />
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
    "/api/method/lsc_api.lsc_api.get_terms.get_terms?term_name=terms_of_use"
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
      <h3 class="text-lg font-bold text-center pb-2">
        وثيقة التغطية القانونية
        <br />
        لــ "مركز المساندة القانونية"
        <br />
        الشروط والاحكام
      </h3>
      <!-- Modal Header -->
      <h2 class="text-xl font-semibold mb-4 text-center">
        الضوابط والاستثناءات
      </h2>

      <!-- Introduction -->
      <p class="mb-4">
        تتضمن وثيقة التغطية القانونية لمركز المساندة القانونية مجموعة من الضوابط
        والاستثناءات والتي تحدد شروط التغطية القانونية، وتلعب هذه الضوابط
        والاستثناءات دورًا مهمًا في حماية حقوق ومصالح كل من الطرفين.
      </p>

      <!-- First Section: ضوابط استخدام وثيقة المساندة -->
      <h3 class="text-lg font-semibold mb-2">
        أولا: ضوابط استخدام وثيقة المساندة
      </h3>

      <!-- ضوابط استخدام وثيقة التأمين القانوني من قبل المشترك -->
      <h4 class="font-semibold mt-4 mb-2">
        أ/ضوابط استخدام وثيقة التأمين القانوني من قبل المشترك:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          يجب على المشترك قراءة الوثيقة بعناية قبل الاشتراك، وذلك للتأكد من فهمه
          لجميع شروطها وأحكامها.
        </li>
        <li>
          يجب على المشترك التأكد من أن الباقة تغطي المخاطر التي يرغب في تغطيتها
          قانونياً، وذلك لتجنب أي مشكلات في المستقبل.
        </li>
        <li>
          يجب على المشترك التبليغ عن أي تغييرات في بياناته الشخصية، مثل عنوانه
          أو رقم هاتفه، أو كفالته إلى مركز المساندة، وذلك لتجنب أي مشكلات في
          المستقبل.
        </li>
        <li>
          الشفافية والصدق والأمانة والإخلاص ومبدأ حسن النية هو ما يلتزم به
          المشترك في تعاملاته مع خدمات مركز المساندة.
        </li>
        <li>
          يلتزم المشترك بالإفصاح عن كافة المعلومات والبيانات المطلوبة منه من قبل
          المركز.
        </li>
        <li>
          يلتزم المشترك بتقديم كافة المستندات المطلوبة من قبل مركز المساندة
          القانونية وفي الوقت المحدد.
        </li>
        <li>
          يتحمل المشترك جميع الأضرار عن الأخطاء التي تصدر منه والتي تحول دون
          استخدام الوثيقة مثل عدم تقديم المستندات أو الكذب في ذكر وقائع الموضوع
          وغيرها.
        </li>
        <li>
          يجب على المشترك الإبلاغ عن الواقعة القانونية خلال 30 يومًا من تاريخ
          وقوعها.
        </li>
        <li>
          يجب على المشترك التعاون مع مركز المساندة القانونية، والاستجابة
          للتعليمات التي يصدرها سواءً بحضور الجلسات في المحكمة إن استدعى ذلك أو
          عدم حضورها أو تقديم الأدلة وغيرها.
        </li>
      </ul>

      <!-- ضوابط استخدام وثيقة التأمين القانوني من قبل مركز المساندة القانونية -->
      <h4 class="font-semibold mt-4 mb-2">
        ب/ضوابط استخدام وثيقة التأمين القانوني من قبل مركز المساندة القانونية:
      </h4>
      <ul class="list-decimal pl-5 mb-4">
        <li>
          يلتزم مركز المساندة القانونية بحماية خصوصية المشترك والحفاظ على سرية
          جميع المعلومات المتعلقة به، بما في ذلك المعلومات الشخصية والوثائق
          والمستندات.
        </li>
        <li>
          يلتزم مركز المساندة بطلب موافقة المشترك على استخدام بيانات التواصل فقط
          الخاصة به لأغراض تسهيل عمليات التفاعل في ما يخص المشترك من خدمات
          ولغايات التسويق لخدمات المركز لمشاركة أية جديد يصدر عن مركز المساندة
          القانونية حسب قانون حماية البيانات الشخصية في المملكة العربية السعودية
          في 16 سبتمبر 2021  والموافق  التاسع من صفر 1443 هجري (9-2-1443)
        </li>
        <li>
          يستطيع المشترك الغاء الموافقة على مشاركة البيانات مع المركز في حالة
          عدم رغبته بذلك من خلال العديد من الوسائل ( الاتصال على المركز ،   من
          خلال حساب المشترك في بوابة المستخدم الخاصة بالنظام الالكتروني للمركز
          ،من خلال ارسال رسالة واتس اب او رسالة نصية للرقم الرسمي المعتمد للمركز
          ) كما ينص عليه قانون حماية البيانات الشخصية في المملكة العربية
          السعودية .
        </li>
        <li>
          يلتزم مركز المساندة القانونية من خلال الموقع الالكتروني بإظهار اشعار
          الخصوصية للزوار لإخطارهم باستخدم ملفات تعريف الإرتباط بغرض جمع
          بياناتهم والحصول على موافقتهم (الضمنية أو الصريحة) بمعالجتها وفقا لما
          ينص عليه قانون حماية البيانات الشخصية في المملكة العربية السعودية .
        </li>
        <li>
          يلتزم مركز المساندة القانونية بالمعايير المهنية والأخلاقية في تقديم
          باقات من الخدمات القانونية.
        </li>
        <li>
          الالتزام بتقديم الحماية القانونية للمشترك حسب الباقة في حالة وقوع
          واقعة قانونية خلال فترة الاشتراك، وذلك وفقًا لشروط الوثيقة.
        </li>
        <li>
          يمكن للمركز تقديم خدمات قانونية إضافية مع فرض رسوم إضافية على المشترك
          في حالة تقديم المساعدة القانونية خارج حدود التغطية المحددة في الوثيقة.
        </li>
        <li>
          يلتزم مركز المساندة القانونية بإخطار المشترك بجميع الإجراءات القانونية
          التي سيتم اتخاذها في شأن الواقعة القانونية.
        </li>
        <li>
          يلتزم مركز المساندة القانونية بإبلاغ المشترك بكافة التطورات المتعلقة
          بالواقعة القانونية.
        </li>
        <li>
          يلتزم المركز بتقديم أفضل باقات من الخدمات القانونية للمشتركين،
          وبالتحسين المستمر لجودة باقات من الخدمات القانونية المقدمة.
        </li>
        <li>
          يلتزم مركز المساندة القانونية بالرد على استفسارات المشتركين في أسرع
          وقت ممكن.
        </li>
        <li>
          يلتزم مركز المساندة القانونية بتوفير المعلومات القانونية للمشتركين
          بشكل واضح ومفهوم.
        </li>
        <li>
          يلتزم مركز المساندة القانونية باحترام حقوق المشتركين وعدم التمييز
          بينهم.
        </li>
      </ul>

      <!-- استثناءات -->
      <h3 class="text-lg font-semibold mb-2">الاستثناءات:</h3>
      <ul class="list-decimal pl-5 mb-4">
        <li>الدعاوى المتعلقة بالجانب السياسي وأمن الدولة.</li>
        <li>
          الدعاوى المتعلقة بالأنشطة غير المشروعة مثل قضايا الإرهاب والمقامرة
          والمخدرات وجرائم الإخلال بالأمن.
        </li>
        <li>
          الدعاوى المخالفة للقوانين والأنظمة والتي قد تم إشعار العميل بها من
          خلال مركز المساندة القانونية.
        </li>
        <li>
          الدعاوى المتعلقة بالقوى القاهرة والظروف الطارئة مثل (فيروس كورونا
          المستجد، الزلازل، البراكين).
        </li>
        <li>
          طلبات الخدمة القانونية الفردية (خارج الباقة) التي تم رفعها قبل تاريخ
          الاشتراك بالباقة.
        </li>
        <li>الواقعة القانونية التي وقعت قبل تاريخ البدء في سريان الوثيقة.</li>
        <li>
          الواقعة القانونية التي وقعت خارج نطاق التغطية المحددة في الوثيقة.
        </li>
        <li>
          الدعاوى الصورية التي تستند إلى عقد ظاهر وحقائق خفية تم الاتفاق عليها
          مسبقاً.
        </li>
        <li>
          الدعاوى الكيدية التي لا تستند إلى أي أساس قانوني أو واقعي، وإنما ترفع
          بهدف الإضرار بالخصم.
        </li>
        <li>
          في حال عدم تعاون المشترك في تقديم المستندات المطلوبة، أو في حال عدم
          وجود مبررات قانونية أو إذا كان المشترك قد ارتكب أي خطأ أو إهمال أدى
          إلى وقوع الواقعة القانونية.
        </li>
        <li>
          في حال وجود قوة قاهرة وظروف طارئة مثل (فيروس كورونا المستجد، الزلازل،
          البراكين) فإن تقديم بعض أو جميع خدمات مركز المساندة قد يتقيد ويتبع في
          ذلك إجراءات وقوانين جراءها.
        </li>
      </ul>

      <!-- الشروط العامة -->
      <h3 class="text-lg font-semibold mb-2">الشروط العامة</h3>
      <p class="mb-4">
        تتضمن وثيقة التغطية القانونية مجموعة من الشروط العامة التي تحدد الحقوق
        والالتزامات لكل من المشترك ومركز المساندة، وتلعب هذه الشروط دورًا مهمًا
        في تنظيم العلاقة بين الطرفين، وفيما يلي الشروط العامة للتغطية القانونية
        في مركز المساندة القانونية:
      </p>

      <ul class="list-decimal pl-5 mb-4 space-y-2">
        <li>
          يقدم مركز المساندة القانونية خدماته القانونية لجميع المواطنين
          والمقيمين في المملكة العربية السعودية.
        </li>
        <li>
          يتم تغطية المشترك بالخدمات التي يقدمها مركز المساندة القانونية للطلبات
          التي تنشأ بعد الاشتراك وخلال الاشتراك حسب باقة المشترك.
        </li>
        <li>
          يبدأ سريان الاشتراك من تاريخ التفعيل وتكون مدة سريان الاشتراك سنة
          ميلادية كاملة.
        </li>
        <li>
          ينتهي تلقائيًا سريان مفعول الوثيقة والخدمات المقدمة بموجبها في حالات
          محددة مثل انتهاء مدة الوثيقة أو وفاة المشترك.
        </li>
        <li>
          في حال انتهاء الاشتراك في الباقة مع وجود طلب قائم وقيد التنفيذ، يتم
          تمديد الاشتراك لمدة (5) أيام حتى يتم سداد رسوم التجديد للباقة.
        </li>
        <li>
          يسدد قيمة الاشتراك لأول مرة قبل تفعيل الوثيقة مباشرة، ثم تدفع سنويا في
          نفس الموعد.
        </li>
        <li>
          في حال رغبة المشترك في ترقية الباقة إلى أخرى خلال فترة سريان الاشتراك،
          يمكن الترقية وفقًا لحالات محددة.
        </li>
        <li>
          الوثيقة غير قابلة للإلغاء أثناء سريانها من قبل المشترك إلا في حالات
          محددة.
        </li>
        <li>
          يلتزم مركز المساندة بالاحتفاظ بالسجلات الخاصة بالمشتركين والتي توضح
          الخدمات المقدمة لهم لمدة خمس سنوات من تاريخ انتهاء سريان مدة الاشتراك
          السنوي.
        </li>
        <li>
          القائم بالاشتراك هو المستفيد نفسه، والانتفاع من الوثيقة ليس قابلاً
          للانتقال أو التنازل عنه لأي طرف آخر.
        </li>
      </ul>
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
      <h3 class="text-lg font-bold text-left pb-2">
        Legal Coverage Document
        <br />
        for "Legal Support Center"
        <br />
        Terms and Conditions
      </h3>
      <!-- Modal Header -->
      <h2 class="text-xl font-semibold mb-4 text-left">
        Regulations and Exceptions
      </h2>

      <!-- Introduction -->
      <p class="mb-4 text-left">
        The legal coverage document for the Legal Support Center includes a set
        of regulations and exceptions that define the terms of legal coverage.
        These regulations and exceptions play an important role in protecting
        the rights and interests of both parties.
      </p>

      <!-- First Section: Regulations for Using the Support Document -->
      <h3 class="text-lg font-semibold mb-2 text-left">
        First: Regulations for Using the Support Document
      </h3>

      <!-- Regulations for using the legal insurance document by the subscriber -->
      <h4 class="font-semibold mt-4 mb-2 text-left">
        A/ Regulations for Using the Legal Insurance Document by the Subscriber:
      </h4>
      <ul class="list-decimal pl-5 mb-4 text-left">
        <li>
          The subscriber must read the document carefully before subscribing to
          ensure they understand all of its terms and conditions.
        </li>
        <li>
          The subscriber must ensure that the package covers the risks they wish
          to have legally covered, to avoid any future issues.
        </li>
        <li>
          The subscriber must report any changes to their personal information,
          such as their address or phone number, to the Legal Support Center, to
          avoid any future problems.
        </li>
        <li>
          Transparency, honesty, integrity, and good faith are what the
          subscriber commits to in their dealings with the services of the Legal
          Support Center.
        </li>
        <li>
          The subscriber is obliged to provide all information and data required
          by the center.
        </li>
        <li>
          The subscriber must submit all documents requested by the Legal
          Support Center within the specified time frame.
        </li>
        <li>
          The subscriber bears all damages caused by errors that prevent the use
          of the document, such as failing to provide documents or lying about
          the facts of the matter, etc.
        </li>
        <li>
          The subscriber must report the legal incident within 30 days from the
          date it occurred.
        </li>
        <li>
          The subscriber must cooperate with the Legal Support Center and
          respond to the instructions issued, whether by attending court
          sessions if necessary or not attending, or providing evidence, etc.
        </li>
      </ul>

      <!-- Regulations for using the legal insurance document by the Legal Support Center -->
      <h4 class="font-semibold mt-4 mb-2 text-left">
        B/ Regulations for Using the Legal Insurance Document by the Legal
        Support Center:
      </h4>
      <ul class="list-decimal pl-5 mb-4 text-left">
        <li>
          The Legal Support Center is committed to protecting the privacy of the
          subscriber and maintaining the confidentiality of all information
          related to them, including personal information, documents, and
          records.
        </li>
        <li>
          The Legal Support Center is obliged to seek the subscriber's consent
          to use their contact data solely for the purpose of facilitating
          interactions regarding services related to the subscriber and for
          marketing the center's services to share any updates from the Legal
          Support Center in accordance with the Personal Data Protection Law in
          the Kingdom of Saudi Arabia on September 16, 2021, corresponding to
          the ninth of Safar 1443 Hijri (9-2-1443).
        </li>
        <li>
          The subscriber can withdraw consent for sharing data with the center
          if they do not wish to do so through various means (contacting the
          center, through their user account in the electronic system's user
          portal, sending a WhatsApp message, or a text message to the center's
          official approved number), as stipulated by the Personal Data
          Protection Law in the Kingdom of Saudi Arabia.
        </li>
        <li>
          The Legal Support Center is obliged to display a privacy notice on its
          website to inform visitors about the use of cookies for the purpose of
          collecting their data and obtaining their consent (implicit or
          explicit) to process it according to the provisions of the Personal
          Data Protection Law in the Kingdom of Saudi Arabia.
        </li>
        <li>
          The Legal Support Center is committed to professional and ethical
          standards in providing packages of legal services.
        </li>
        <li>
          Commitment to providing legal protection for the subscriber according
          to the package in the event of a legal incident during the
          subscription period, according to the terms of the document.
        </li>
        <li>
          The center can provide additional legal services with extra charges to
          the subscriber in the case of providing legal assistance outside the
          coverage specified in the document.
        </li>
        <li>
          The Legal Support Center is obliged to inform the subscriber of all
          legal actions that will be taken concerning the legal incident.
        </li>
        <li>
          The Legal Support Center is obliged to inform the subscriber of all
          developments related to the legal incident.
        </li>
        <li>
          The center is committed to providing the best packages of legal
          services to subscribers and continuously improving the quality of the
          legal service packages provided.
        </li>
        <li>
          The Legal Support Center is committed to responding to subscribers'
          inquiries as quickly as possible.
        </li>
        <li>
          The Legal Support Center is committed to providing legal information
          to subscribers clearly and understandably.
        </li>
        <li>
          The Legal Support Center is committed to respecting the rights of
          subscribers and not discriminating between them.
        </li>
      </ul>

      <!-- Exceptions -->
      <h3 class="text-lg font-semibold mb-2 text-left">Exceptions:</h3>
      <ul class="list-decimal pl-5 mb-4 text-left">
        <li>Claims related to political matters and state security.</li>
        <li>
          Claims related to illegal activities such as terrorism, gambling,
          drug-related issues, and crimes against public security.
        </li>
        <li>
          Claims that violate laws and regulations which the client has been
          notified of by the Legal Support Center.
        </li>
        <li>
          Claims related to force majeure and emergency circumstances such as
          (COVID-19, earthquakes, volcanoes).
        </li>
        <li>
          Individual legal service requests (outside the package) submitted
          before the subscription date.
        </li>
        <li>
          Legal incidents that occurred before the effective date of the
          document.
        </li>
        <li>
          Legal incidents that occurred outside the coverage specified in the
          document.
        </li>
        <li>
          Frivolous claims based on apparent contracts and hidden facts that
          were agreed upon in advance.
        </li>
        <li>
          Malicious claims that have no legal or factual basis, but are raised
          to harm the opponent.
        </li>
        <li>
          In the case of non-cooperation by the subscriber in providing the
          required documents, or if there are no legal justifications, or if the
          subscriber has committed any mistake or negligence that led to the
          occurrence of the legal incident.
        </li>
        <li>
          In case of force majeure and emergency circumstances such as
          (COVID-19, earthquakes, volcanoes), the provision of some or all of
          the Legal Support Center's services may be restricted and will follow
          the applicable procedures and regulations.
        </li>
      </ul>

      <!-- General Conditions -->
      <h3 class="text-lg font-semibold mb-2 text-left">General Conditions</h3>
      <p class="mb-4 text-left">
        The legal coverage document includes a set of general conditions that
        define the rights and obligations of both the subscriber and the Legal
        Support Center. These conditions play an important role in regulating
        the relationship between the two parties. Below are the general
        conditions for legal coverage at the Legal Support Center:
      </p>

      <ul class="list-decimal pl-5 mb-4 space-y-2 text-left">
        <li>
          The Legal Support Center provides its legal services to all citizens
          and residents in the Kingdom of Saudi Arabia.
        </li>
        <li>
          The subscriber is covered by the services provided by the Legal
          Support Center for requests that arise after subscription and during
          the subscription period according to the subscriber's package.
        </li>
        <li>
          The subscription becomes effective from the activation date and lasts
          for a full calendar year.
        </li>
        <li>
          The validity of the document and the services provided under it will
          automatically end in certain cases, such as the expiration of the
          document or the death of the subscriber.
        </li>
        <li>
          If the subscription to the package ends while there is an ongoing
          request, the subscription will be extended for (5) days until the
          renewal fees for the package are paid.
        </li>
        <li>
          The subscription fee must be paid for the first time before activating
          the document, and then it is paid annually at the same time.
        </li>
        <li>
          If the subscriber wishes to upgrade the package to another one during
          the subscription period, upgrades can be made according to specific
          cases.
        </li>
        <li>
          The document is non-cancellable during its validity by the subscriber
          except in specific cases.
        </li>
        <li>
          The Legal Support Center is obliged to keep records of subscribers
          that clarify the services provided to them for five years from the
          expiration of the annual subscription period.
        </li>
        <li>
          The subscriber is the actual beneficiary, and the benefits of the
          document are not transferable or assignable to any other party.
        </li>
      </ul>
    </div>
  </div>
*/
</script>
