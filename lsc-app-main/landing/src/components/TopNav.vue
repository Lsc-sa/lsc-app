<template>
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="navbar fixed top-0 left-0 right-0 place-self-center bg-white z-10 text-black"
  >
    <div class="navbar lg:w-4/5 mx-auto">
      <div class="navbar-start">
        <div class="dropdown inline-block lg:hidden">
          <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h7"
              />
            </svg>
          </div>
          <ul
            tabindex="0"
            class="menu menu-sm dropdown-content rounded-box z-[1] mt-3 w-52 p-2 shadow bg-white"
          >
            <li>
              <a href="#home"> {{ $t("Home") }} </a>
            </li>
            <li>
              <a href="#about">{{ $t("About") }} </a>
            </li>
            <li>
              <a href="#services">{{ $t("Services") }} </a>
            </li>
            <li>
              <a href="#packages">{{ $t("Packages") }} </a>
            </li>
            <li>
              <a href="#contact">{{ $t("Contact") }} </a>
            </li>
            <a
              class="btn font-semibold bg-primary text-white"
              href="https://portal.lsc-sa.net/dashboard"
            >
              {{ $t("Signup") }}
            </a>
            <button
              class="btn font-semibold bg-primary text-white"
              onclick="my_modal_2.showModal()"
            >
              {{ $t("Early Register") }}
            </button>
          </ul>
        </div>
        <a
          class="btn mx-2 font-semibold border-0 bg-primary hidden hover:bg-primaryHover text-white flex lg:flex"
          href="https://portal.lsc-sa.net/dashboard"
        >
          {{ $t("Signup") }}
        </a>
        <button
          class="btn font-semibold border-0 bg-primary hidden lg:block hover:bg-primaryHover text-white"
          onclick="my_modal_2.showModal()"
        >
          {{ $t("Early Register") }}
        </button>
      </div>
      <div class="navbar-center hidden lg:flex">
        <ul class="menu menu-horizontal px-1 flex-row-reverse">
          <li>
            <a href="#home"> {{ $t("Home") }} </a>
          </li>
          <li>
            <a href="#about">{{ $t("About") }} </a>
          </li>
          <li>
            <a href="#services">{{ $t("Services") }} </a>
          </li>
          <li>
            <a href="#packages">{{ $t("Packages") }} </a>
          </li>
          <li>
            <a href="#contact">{{ $t("Contact") }} </a>
          </li>
        </ul>
      </div>
      <div class="navbar-end">
        <LanguageSelect class="mx-4" />
        <RouterLink to="/" class="btn btn-ghost">
          <img
            src="../assets/images/logo.png"
            alt="Logo"
            class="block w-[40px]"
          />
        </RouterLink>
      </div>
    </div>
  </div>

  <dialog
    id="my_modal_2"
    class="modal"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
  >
    <div class="modal-box overflow-x-hidden">
      <h3 class="text-lg font-bold">
        {{ $t("FormFill.Welcome") }}
      </h3>
      <p class="py-4">
        {{ $t("FormFill.Waiting") }}
      </p>
      <form @submit.prevent="handleSubmit">
        <!-- First Name Input -->
        <div class="mb-2">
          <label for="name" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.Name") }}
          </label>
          <input
            type="text"
            id="name"
            v-model="form.first_name"
            class="input input-bordered w-full input-sm bg-transparent"
            :placeholder="t('FormFill.Name')"
            autocomplete="name"
          />
          <!-- Error Message for First Name -->
          <p v-if="errors.first_name" class="text-red-500 text-xs mt-2">
            {{ errors.first_name }}
          </p>
        </div>
        <!-- Email Input -->
        <div class="mb-2">
          <label for="email" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.Email") }}
          </label>
          <input
            type="text"
            id="email"
            v-model="form.email"
            class="input input-bordered w-full input-sm bg-transparent"
            :placeholder="t('FormFill.Email')"
            autocomplete="email"
          />
          <!-- Error Message for Email -->
          <p v-if="errors.email" class="text-red-500 text-xs mt-2">
            {{ errors.email }}
          </p>
        </div>
        <!-- Mobile Number Input -->
        <div class="mb-2">
          <label for="tel" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.Phone") }}
          </label>
          <input
            type="text"
            id="tel"
            v-model="form.mobile_no"
            class="input input-bordered w-full input-sm bg-transparent"
            :placeholder="t('FormFill.Phone')"
            autocomplete="phone"
          />
          <!-- Error Message for Mobile Number -->
          <p v-if="errors.mobile_no" class="text-red-500 text-xs mt-2">
            {{ errors.mobile_no }}
          </p>
        </div>
        <!-- Nationality -->
        <div class="mb-2">
          <label for="job" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.Nationality") }}
          </label>
          <select
            class="select select-bordered w-full select-sm bg-transparent"
            id="job"
            v-model="form.nationality"
          >
            <option v-for="country in countries" :value="country.name">
              {{ country.country_name }}
            </option>
          </select>
          <!-- Error Message for Job Title -->
          <p v-if="errors.nationality" class="text-red-500 text-xs mt-2">
            {{ errors.nationality }}
          </p>
        </div>
        <!-- City Input -->
        <div class="mb-2">
          <label for="city" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.City") }}
          </label>

          <select
            class="select select-bordered w-full select-sm bg-transparent"
            id="city"
            v-model="form.city"
          >
            <option v-for="city in allCities" :value="city.arabic_name">
              {{ $i18n.locale == "en" ? city.english_name : city.arabic_name }}
            </option>
          </select>
          <!-- Error Message for City -->
          <p v-if="errors.city" class="text-red-500 text-xs mt-2">
            {{ errors.city }}
          </p>
        </div>
        <!-- Job Title Input -->
        <div class="mb-2">
          <label for="job" class="block mb-2 text-sm font-medium">
            {{ $t("FormFill.Job") }}
          </label>
          <input
            type="text"
            id="job"
            v-model="form.job_title"
            class="input input-bordered w-full input-sm bg-transparent"
            :placeholder="t('FormFill.Job')"
            autocomplete="organization-title"
          />
          <!-- Error Message for Job Title -->
          <p v-if="errors.job_title" class="text-red-500 text-xs mt-2">
            {{ errors.job_title }}
          </p>
        </div>

        <!-- General Error Message -->
        <p v-if="errors.general" class="text-red-500 text-center text-xs mt-2">
          {{ errors.general }}
        </p>

        <div class="flex items-center gap-4">
          <input
            name="check"
            type="checkbox"
            checked="checked"
            class="checkbox checkbox-sm"
          />
          <label for="check" class="block text-sm font-medium">
            {{ $t("FormFill.RecieveUpdates") }}
          </label>
        </div>
        <div class="flex items-center gap-4">
          <input
            name="check"
            type="checkbox"
            checked="checked"
            v-model="form.accept_terms"
            class="checkbox checkbox-sm"
          />
          <label for="check" class="block text-sm font-medium mb-2">
            {{ $t("FormFill.AcceptTerms") }}
            <button
              class="btn btn-sm btn-primary"
              type="button"
              onclick="my_modal_1.showModal()"
            >
              {{ $t("FormFill.AcceptTermsbtn") }}
            </button>
          </label>
          <!-- <p v-if="errors.accept_terms" class="text-red-500 text-xs mt-2">
            {{ errors.accept_terms }}
          </p> -->
        </div>
        <!-- Submit Button -->
        <button
          type="submit"
          class="btn block mx-auto min-w-32 btn-primary text-white"
        >
          {{ $t("Signup") }}
        </button>
      </form>
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
    </div>
    <form method="dialog" class="modal-backdrop">
      <button ref="btnn" @click="clicked">close</button>
    </form>
  </dialog>
  <!-- الشروط والاحكام -->
  <dialog
    id="my_modal_1"
    class="modal text-black"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
  >
    <div class="modal-box" v-if="$i18n.locale == 'ar'">
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <h3 class="text-lg font-bold text-center pb-2">
        وثيقة التغطية القانونية لــ "مركز المساندة القانونية" الشروط والاحكام
      </h3>
      <div
        class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      >
        <!-- Modal Header -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          الضوابط والاستثناءات
        </h2>

        <!-- Introduction -->
        <p class="mb-4">
          تتضمن وثيقة التغطية القانونية لمركز المساندة القانونية مجموعة من
          الضوابط والاستثناءات والتي تحدد شروط التغطية القانونية، وتلعب هذه
          الضوابط والاستثناءات دورًا مهمًا في حماية حقوق ومصالح كل من الطرفين.
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
            يجب على المشترك قراءة الوثيقة بعناية قبل الاشتراك، وذلك للتأكد من
            فهمه لجميع شروطها وأحكامها.
          </li>
          <li>
            يجب على المشترك التأكد من أن الباقة تغطي المخاطر التي يرغب في
            تغطيتها قانونياً، وذلك لتجنب أي مشكلات في المستقبل.
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
            يلتزم المشترك بالإفصاح عن كافة المعلومات والبيانات المطلوبة منه من
            قبل المركز.
          </li>
          <li>
            يلتزم المشترك بتقديم كافة المستندات المطلوبة من قبل مركز المساندة
            القانونية وفي الوقت المحدد.
          </li>
          <li>
            يتحمل المشترك جميع الأضرار عن الأخطاء التي تصدر منه والتي تحول دون
            استخدام الوثيقة مثل عدم تقديم المستندات أو الكذب في ذكر وقائع
            الموضوع وغيرها.
          </li>
          <li>
            يجب على المشترك الإبلاغ عن الواقعة القانونية خلال 30 يومًا من تاريخ
            وقوعها.
          </li>
          <li>
            يجب على المشترك التعاون مع مركز المساندة القانونية، والاستجابة
            للتعليمات التي يصدرها سواءً بحضور الجلسات في المحكمة إن استدعى ذلك
            أو عدم حضورها أو تقديم الأدلة وغيرها.
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
            يلتزم مركز المساندة بطلب موافقة المشترك على استخدام بيانات التواصل
            فقط الخاصة به لأغراض تسهيل عمليات التفاعل في ما يخص المشترك من خدمات
            ولغايات التسويق لخدمات المركز لمشاركة أية جديد يصدر عن مركز المساندة
            القانونية حسب قانون حماية البيانات الشخصية في المملكة العربية
            السعودية في 16 سبتمبر 2021  والموافق  التاسع من صفر 1443 هجري
            (9-2-1443)
          </li>
          <li>
            يستطيع المشترك الغاء الموافقة على مشاركة البيانات مع المركز في حالة
            عدم رغبته بذلك من خلال العديد من الوسائل ( الاتصال على المركز ،   من
            خلال حساب المشترك في بوابة المستخدم الخاصة بالنظام الالكتروني للمركز
            ،من خلال ارسال رسالة واتس اب او رسالة نصية للرقم الرسمي المعتمد
            للمركز ) كما ينص عليه قانون حماية البيانات الشخصية في المملكة
            العربية السعودية .
          </li>
          <li>
            يلتزم مركز المساندة القانونية من خلال الموقع الالكتروني بإظهار اشعار
            الخصوصية للزوار لإخطارهم باستخدم ملفات تعريف الإرتباط بغرض جمع
            بياناتهم والحصول على موافقتهم (الضمنية أو الصريحة) بمعالجتها وفقا
            لما ينص عليه قانون حماية البيانات الشخصية في المملكة
            العربية السعودية .
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
            يمكن للمركز تقديم خدمات قانونية إضافية مع فرض رسوم إضافية على
            المشترك في حالة تقديم المساعدة القانونية خارج حدود التغطية المحددة
            في الوثيقة.
          </li>
          <li>
            يلتزم مركز المساندة القانونية بإخطار المشترك بجميع الإجراءات
            القانونية التي سيتم اتخاذها في شأن الواقعة القانونية.
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
            الدعاوى الكيدية التي لا تستند إلى أي أساس قانوني أو واقعي، وإنما
            ترفع بهدف الإضرار بالخصم.
          </li>
          <li>
            في حال عدم تعاون المشترك في تقديم المستندات المطلوبة، أو في حال عدم
            وجود مبررات قانونية أو إذا كان المشترك قد ارتكب أي خطأ أو إهمال أدى
            إلى وقوع الواقعة القانونية.
          </li>
          <li>
            في حال وجود قوة قاهرة وظروف طارئة مثل (فيروس كورونا المستجد،
            الزلازل، البراكين) فإن تقديم بعض أو جميع خدمات مركز المساندة قد
            يتقيد ويتبع في ذلك إجراءات وقوانين جراءها.
          </li>
        </ul>

        <!-- الشروط العامة -->
        <h3 class="text-lg font-semibold mb-2">الشروط العامة</h3>
        <p class="mb-4">
          تتضمن وثيقة التغطية القانونية مجموعة من الشروط العامة التي تحدد الحقوق
          والالتزامات لكل من المشترك ومركز المساندة، وتلعب هذه الشروط دورًا
          مهمًا في تنظيم العلاقة بين الطرفين، وفيما يلي الشروط العامة للتغطية
          القانونية في مركز المساندة القانونية:
        </p>

        <ul class="list-decimal pl-5 mb-4 space-y-2">
          <li>
            يقدم مركز المساندة القانونية خدماته القانونية لجميع المواطنين
            والمقيمين في المملكة العربية السعودية.
          </li>
          <li>
            يتم تغطية المشترك بالخدمات التي يقدمها مركز المساندة القانونية
            للطلبات التي تنشأ بعد الاشتراك وخلال الاشتراك حسب باقة المشترك.
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
            يسدد قيمة الاشتراك لأول مرة قبل تفعيل الوثيقة مباشرة، ثم تدفع سنويا
            في نفس الموعد.
          </li>
          <li>
            في حال رغبة المشترك في ترقية الباقة إلى أخرى خلال فترة سريان
            الاشتراك، يمكن الترقية وفقًا لحالات محددة.
          </li>
          <li>
            الوثيقة غير قابلة للإلغاء أثناء سريانها من قبل المشترك إلا في حالات
            محددة.
          </li>
          <li>
            يلتزم مركز المساندة بالاحتفاظ بالسجلات الخاصة بالمشتركين والتي توضح
            الخدمات المقدمة لهم لمدة خمس سنوات من تاريخ انتهاء سريان مدة
            الاشتراك السنوي.
          </li>
          <li>
            القائم بالاشتراك هو المستفيد نفسه، والانتفاع من الوثيقة ليس قابلاً
            للانتقال أو التنازل عنه لأي طرف آخر.
          </li>
        </ul>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">إغلاق</button>
        </form>
      </div>
    </div>
    <div class="modal-box" v-else>
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <div class="p-6 bg-white rounded-lg shadow-lg max-w-3xl mx-auto">
        <!-- Modal Header -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          Controls and Exceptions
        </h2>

        <!-- Preface -->
        <p class="mb-4">
          The legal coverage document of the Musanadah Legal Support Center
          includes a set of controls and exceptions that define the conditions
          of legal coverage, and these controls and exceptions play an important
          role in protecting the rights and interests of both parties.
        </p>

        <!-- First Section: Controls on the Use of the Musanadah Document -->
        <h3 class="text-lg font-semibold mb-2">
          First: Controls on the Use of the Musanadah Document
        </h3>
        <p class="mb-4">
          The Musanadah Legal document is subject to certain controls that must
          be adhered to by the subscriber and the Musanadah Legal Support
          Center, in order to ensure the rights of the parties and achieve the
          purpose of the legal insurance.
        </p>

        <!-- A/ Controls the Use of the Legal Insurance Document by the Subscriber -->
        <h4 class="font-semibold mt-4 mb-2">
          A/ Controls the Use of the Legal Insurance Document by the Subscriber:
        </h4>
        <ul class="list-disc pl-5 mb-4">
          <li>
            The subscriber should read the document carefully before signing up,
            so as to make sure he understands all its terms and conditions.
          </li>
          <li>
            The subscriber should make sure that the package covers the risks he
            wishes to cover legally, so as to avoid any problems in the future.
          </li>
          <li>
            The subscriber must report any changes to his personal data, such as
            his address or phone number, or sponsorship to the Musanadah center,
            to avoid any issues that might cause conflicts in the future.
          </li>
          <li>
            Transparency, honesty, sincerity, and the principle of good faith is
            what the subscriber is committed to in his dealings with the
            services of the Musanadah center.
          </li>
          <li>
            The subscriber is obliged to disclose all information and data
            required by the center.
          </li>
          <li>
            The subscriber is obliged to submit all the documents required by
            the Musanadah Legal Support Center on time.
          </li>
          <li>
            The subscriber shall bear all damages for his mistakes that prevent
            the use of the document such as failure to submit documents or lying
            in mentioning the facts of the issue and others.
          </li>
          <li>
            The subscriber must report the legal issue within 30 days from the
            date it occurs.
          </li>
          <li>
            The subscriber must cooperate with the Musanadah Legal Support
            Center and respond to the instructions given to him whether to
            attend or not to attend the hearings in court if required or provide
            evidence and others related.
          </li>
        </ul>

        <!-- B/ Controls the Use of the Legal Insurance Document by the Musanadah Legal Support Center -->
        <h4 class="font-semibold mt-4 mb-2">
          B/ Controls the Use of the Legal Insurance Document by the Musanadah
          Legal Center:
        </h4>
        <ul class="list-disc pl-5 mb-4">
          <li>
            The Musanadah Legal Support Center is committed to protecting the
            privacy of the subscriber and maintaining the confidentiality of all
            information related to him, including personal information,
            documents, and records.
          </li>
          <li>
            Musanadah Legal Support Center requests the client’s consent to use
            his/her contact information only for the purpose of facilitating
            interaction with the client regarding services and for marketing the
            Center’s services. To share any new information issued by Musanadah
            Legal Support Center (according to the Personal Data Protection Law
            in the Kingdom of Saudi Arabia on September 16, 2021, corresponding
            to Safar 9, 1443 AH) (9-2-1443).
          </li>
          <li>
            The customer can cancel his consent to share data with the center if
            he does not wish to do so through many means contacting the center,
            through the customer’s account on the user portal of the center’s
            electronic system, by sending a WhatsApp message or a text message
            to the center’s official number (as stipulated in the Personal Data
            Protection Law in the Kingdom of Saudi Arabia).
          </li>
          <li>
            Musanadah Legal Support Center, through its website, displays a
            privacy notice to visitors to inform them that it uses cookies to
            collect data and obtain their consent (implicit or explicit) to
            process it in accordance with the Personal Data Protection Law in
            the Kingdom of Saudi Arabia.
          </li>
          <li>
            The Musanadah Legal Support Center adheres to professional and
            ethical standards in the provision of legal services.
          </li>
          <li>
            The obligation to provide legal protection to the subscribers
            according to the services included in his active package, in
            accordance with the terms of the document.
          </li>
          <li>
            The Center can provide additional legal services with additional
            fees charged to the subscriber in case of legal aid being provided
            outside the coverage limits specified in the document.
          </li>
          <li>
            The Musanadah Legal Support Center is committed to notifying the
            subscribers of all legal actions that will be taken related to the
            legal services as per the procedures.
          </li>
          <li>
            The Musanadah Legal Support Center is obliged to inform the
            subscribers of all updates related to the legal case.
          </li>
          <li>
            The Center is committed to providing the best legal services to
            subscribers and to continuously improving the quality of legal
            services provided.
          </li>
          <li>
            The Musanadah Legal Support Center is committed to responding to the
            inquiries of the subscribers as soon as possible.
          </li>
          <li>
            The Musanadah Legal Support Center is committed to providing legal
            information to subscribers clearly and understandably.
          </li>
          <li>
            The Musanadah Legal Support Center is committed to respecting the
            rights of subscribers and not discriminating between them.
          </li>
        </ul>

        <!-- Exceptions -->
        <h3 class="text-lg font-semibold mb-2">Exceptions</h3>
        <p class="mb-4">
          The exceptions are cases not covered by the services and packages of
          the Musanadah Legal Support Center, including cases where the
          subscriber is responsible for the occurrence of the legal issue, or if
          the requested services are not covered by the legal coverage of the
          document, or due to circumstances beyond the control of all parties,
          including:
        </p>
        <ul class="list-disc pl-5 mb-4">
          <li>
            Cases related to the political aspect and security and safety of the
            Kingdom.
          </li>
          <li>
            Lawsuits related to illegal activities such as terrorism, gambling,
            drugs, and breach of security offenses.
          </li>
          <li>
            Actions that violate laws and regulations and that have been
            notified to the customer through the Musanadah Legal Support Center.
          </li>
          <li>
            Claims relating to force majeure and emergency conditions (e.g.,
            COVID-19, recent earthquakes, and volcanoes).
          </li>
          <li>
            Individual legal service requests (outside the package) that were
            officially registered prior to the subscription date.
          </li>
          <li>
            The legal fact that occurred before the activation date of the
            document.
          </li>
          <li>
            The legal fact that occurred outside the coverage scope specified in
            the document.
          </li>
          <li>
            Sham claims based on apparent contracts and hidden facts previously
            agreed upon.
          </li>
          <li>
            Conspirator claims, which are not based on any legal or factual
            basis, raised with the aim of harming the opponent.
          </li>
          <li>
            In case subscribers do not cooperate in the submission of the
            required documents, or in the absence of legal justification, or if
            the subscriber has committed any action or negligence that led to
            the occurrence of the legal fact.
          </li>
          <li>
            In emergency conditions (e.g., COVID-19, earthquakes, volcanoes),
            the provision of some or all of the services of the Musanadah Legal
            Center may be restricted and subject to the procedures and laws
            followed.
          </li>
        </ul>

        <!-- General Conditions -->
        <h3 class="text-lg font-semibold mb-2">General Conditions</h3>
        <p class="mb-4">
          The legal coverage document includes a set of general conditions that
          define the rights and obligations of both the subscribers and the
          Musanadah Legal Support Center, and these conditions play an important
          role in regulating the relationship between the parties. The following
          are the general conditions of legal coverage in the Musanadah Legal
          Support Center:
        </p>

        <ul class="list-decimal pl-5 mb-4 space-y-2">
          <li>
            The Musanadah Legal Support Center provides legal services to all
            citizens and residents of the Kingdom of Saudi Arabia.
          </li>
          <li>
            The subscriber is covered by the services provided by the Musanadah
            Legal Center for requests submitted after subscription activation
            and during the subscription according to the subscription plan,
            except for legal facts that occurred before the subscription date or
            individual service requests filed before the subscription date.
          </li>
          <li>
            The subscription shall be effective from the date of activation,
            whether it was manually activated by the employees of the Musanadah
            Center, electronically, or by phone, and the validity period of the
            subscription shall be a full calendar year.
          </li>
          <li>
            The subscription and the services provided thereunder shall
            automatically cease to be effective in the following cases:
            <ul class="list-disc pl-5 mt-2">
              <li>
                Expiration of the document period except for transactions
                initiated prior to the expiration of the document.
              </li>
              <li>
                When the subscriber has exhausted his services balance in the
                package.
              </li>
              <li>
                The death of the subscriber, except for transactions initiated
                before the death, unless the legitimate heirs are required to
                complete certain legal requests within sixty days of the death,
                such as the termination of the procedures for receiving labor or
                other rights.
              </li>
              <li>
                Final departure from Saudi Arabia, with the exception of
                transactions initiated before leaving the Kingdom, provided that
                there is a valid residence in the Kingdom for electronic
                authentication through the Absher or Nafath platforms.
              </li>
            </ul>
          </li>
          <li>
            If the subscription to the package ends with an existing application
            and is under progress:
            <ul class="list-disc pl-5 mt-2">
              <li>
                Extending the subscription for 5 days until the renewal fee for
                the package is paid, and in the event of non-payment, the
                services are not binding and work is suspended accordingly.
              </li>
              <li>
                Extension until termination of service: The value of the service
                is estimated.
              </li>
            </ul>
          </li>
          <li>
            The subscription is paid for the first time immediately before
            activation, and then paid annually at the same time. It is forbidden
            to renew the subscription more than 10 days before its expiry,
            provided that the application is submitted to risk management to
            study the subscriber's file during the past year.
          </li>
          <li>
            In case the subscriber wishes to upgrade the package to another
            during the validity of the subscription:
            <ul class="list-disc pl-5 mt-2">
              <li>
                Promotion during the first month of subscription: Any subscriber
                can upgrade the package within 30 days, paying the difference
                between the two packages, and deducting the value of the month
                if there is no active requested service in the old package. When
                there is a previous or existing request, the subscriber cannot
                upgrade the package. The subscriber is not allowed to obtain
                more than one package at the same time, so when upgrading the
                previous package is canceled.
              </li>
              <li>
                Promotion after the first month of subscription: When there is a
                previous or existing order, the subscriber cannot upgrade the
                package. In the absence of a previous or existing application,
                the subscriber can upgrade the plan, by paying the difference
                between the current plan and the new plan in addition to the
                administrative fee in the number of months of the previous
                subscription.
              </li>
            </ul>
          </li>
          <li>
            The subscriber is not permitted to cancel his package as long as it
            is still valid and active. The Musanadah Legal Support Center has
            the right to cancel the subscription if it is found that the
            subscriber has abused the service by providing incorrect
            information. The Musanadah Center has the right to cancel the
            subscription if it is found that the subscriber has subscribed for
            the existence of services expected to be requested within thirty
            days after the subscription.
          </li>
          <li>
            The Musanadah Legal Support Center is committed to maintaining the
            records of the subscribers, including each user and the services
            provided to him (for a period of five years from the date of expiry
            of the annual subscription period); the Center also has no right to
            share information with third parties unless they are judicial
            authorities or at the request of official bodies, where it is
            considered to be within the confidentiality of information between
            the client and the lawyer.
          </li>
          <li>
            The subscriber is the beneficiary himself, and the use of the
            services is exclusively for the subscriber himself, unless the
            subscriber’s package specifies its coverage to other parties:
            husband, wife, or children.
          </li>
          <li>
            The Musanadah Center allows subscribers to request additional legal
            services outside the scope of the package, only once and at an
            additional fee according to the conditions of service, requiring
            direct communication with the center. If the subscriber requests
            additional service outside the coverage of his package, they will
            offer to provide it.
          </li>
          <li>
            Communications between the Musanadah Legal Support Center and
            subscribers are made through the email registered in the system, or
            through WhatsApp messages for the registered mobile number, or
            system notifications. The subscriber must notify the Center of any
            update or change in the contact addresses. The Musanadah Legal
            Support Center is committed to notifying the subscribers of the date
            of renewal of the package before the expiry of its duration by a
            period of not less than 30 days. The Center sends periodic
            notifications to subscribers as a new update or awareness of one of
            the systems and is considered an official notification when pressing
            the icon (read).
          </li>
          <li>
            The subscribers are committed to abide by the conditions contained
            in the document and the commitments decided upon, and in return, the
            Musanadah Center is committed to implementing the approved document
            for the benefit of the subscribers in order to achieve a stable
            legal environment.
          </li>
          <li>
            The document is complete and comprehensive but may contain points
            that can be explained or clarified by the regulation of the
            Musanadah Center.
          </li>
        </ul>
      </div>

      <div class="modal-action">
        <form method="dialog">
          <button class="btn">close</button>
        </form>
      </div>
    </div>
  </dialog>
  <!-- سياسة الاستفسارات -->
  <dialog
    id="my_modal_11"
    class="modal"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
  >
    <div class="modal-box" v-if="$i18n.locale == 'ar'">
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <h3 class="text-lg font-bold text-center pb-2">الشكاوى والاستفسارات</h3>
      <div
        class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      >
        <!-- Modal Header -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          سياسة الإجابة على الاستفسارات ومعالجة الشكاوى
        </h2>

        <!-- Introduction -->
        <p class="mb-4">
          تهدف هذه السياسة إلى تنظيم عملية التعامل مع استفسارات وشكاوى العملاء
          لضمان تقديم خدمة عالية الجودة والاستجابة الفعالة.
        </p>

        <!-- استقبال الاستفسارات والشكاوى -->
        <h3 class="text-lg font-semibold mb-2">
          استقبال الاستفسارات والشكاوى:
        </h3>
        <ul class="list-decimal pl-5 mb-4">
          <li>يمكن تقديم الاستفسارات والشكاوى عبر:</li>
          <li>
            الموقع الإلكتروني:
            <a href="https://portal.lsc-sa.net/" class="text-blue-500 underline"
              >https://portal.lsc-sa.net/</a
            >
          </li>
          <li>
            البريد الإلكتروني:
            <a href="mailto:info@lsc-sa.net" class="text-blue-500 underline"
              >info@lsc-sa.net</a
            >
          </li>
          <li>الهاتف المخصص لخدمة العملاء: 055-955-7313</li>
        </ul>

        <!-- معالجة الشكاوى -->
        <h3 class="text-lg font-semibold mb-2">معالجة الشكاوى:</h3>
        <ul class="list-decimal pl-5 mb-4">
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

        <!-- مراقبة الجودة والتقييم -->
        <h3 class="text-lg font-semibold mb-2">مراقبة الجودة والتقييم:</h3>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            يتم مراجعة الشكاوى والاستفسارات بانتظام لتحسين العمليات وتعزيز جودة
            الخدمة.
          </li>
          <li>
            يتم تقييم مستوى رضا العملاء بعد حل كل شكوى لضمان تحسين مستوى الخدمة
            في المستقبل.
          </li>
        </ul>

        <!-- السرية والخصوصية -->
        <h3 class="text-lg font-semibold mb-2">السرية والخصوصية:</h3>
        <p class="mb-4">
          يتم التعامل مع جميع الاستفسارات والشكاوى بسرية تامة، وتتعهد الشركة
          بعدم مشاركة معلومات المستهلكين مع أي طرف ثالث دون إذن مسبق.
        </p>

        <p class="mb-4">
          هذه السياسة تهدف إلى تعزيز ثقة العملاء في الشركة وضمان الشفافية في
          التعامل مع استفساراتهم وشكاويهم.
        </p>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">إغلاق</button>
        </form>
      </div>
    </div>
    <div class="modal-box" v-else>
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <h3 class="text-lg font-bold text-center pb-2">
        Complaints and Inquiries
      </h3>
      <div
        class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      >
        <!-- Modal Header -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          Inquiry Response and Complaint Handling Policy
        </h2>

        <!-- Introduction -->
        <p class="mb-4">
          This policy aims to organize the handling of customer inquiries and
          complaints to ensure high-quality service and effective responses.
        </p>

        <!-- Receiving Inquiries and Complaints -->
        <h3 class="text-lg font-semibold mb-2">
          Receiving Inquiries and Complaints:
        </h3>
        <ul class="list-decimal pl-5 mb-4">
          <li>Inquiries and complaints can be submitted via:</li>
          <li>
            Website:
            <a href="https://portal.lsc-sa.net/" class="text-blue-500 underline"
              >https://portal.lsc-sa.net/</a
            >
          </li>
          <li>
            Email:
            <a href="mailto:info@lsc-sa.net" class="text-blue-500 underline"
              >info@lsc-sa.net</a
            >
          </li>
          <li>Dedicated customer service phone: 055-955-7313</li>
        </ul>

        <!-- Handling Complaints -->
        <h3 class="text-lg font-semibold mb-2">Handling Complaints:</h3>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            The complaint will be investigated by the specialized team to ensure
            it is analyzed fairly and impartially.
          </li>
          <li>
            The customer will be contacted during the investigation period to
            provide updates on the status of the complaint.
          </li>
          <li>
            Suitable solutions will be provided for each complaint based on the
            investigation results.
          </li>
        </ul>

        <!-- Quality Monitoring and Evaluation -->
        <h3 class="text-lg font-semibold mb-2">
          Quality Monitoring and Evaluation:
        </h3>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            Complaints and inquiries are regularly reviewed to improve processes
            and enhance service quality.
          </li>
          <li>
            Customer satisfaction is evaluated after resolving each complaint to
            ensure future service improvements.
          </li>
        </ul>

        <!-- Confidentiality and Privacy -->
        <h3 class="text-lg font-semibold mb-2">Confidentiality and Privacy:</h3>
        <p class="mb-4">
          All inquiries and complaints are handled with complete
          confidentiality, and the company commits to not sharing consumer
          information with any third party without prior consent.
        </p>

        <p class="mb-4">
          This policy aims to enhance customer trust in the company and ensure
          transparency in handling their inquiries and complaints.
        </p>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">Close</button>
        </form>
      </div>
    </div>
  </dialog>
  <!-- سياسة الاسترجاع -->
  <dialog
    id="my_modal_12"
    class="modal"
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
  >
    <div class="modal-box" v-if="$i18n.locale == 'ar'">
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <h3 class="text-lg font-bold text-center pb-2">
        سياسة الاستبدال والإرجاع
      </h3>
      <div
        class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      >
        <!-- Policy Scope -->
        <h2 class="text-xl font-semibold mb-4 text-center">1. نطاق السياسة</h2>
        <p class="mb-4">
          تنطبق هذه السياسة على جميع الخدمات القانونية المقدمة عبر الموقع بنظام
          الباقات السنوية. يتوجب على العملاء قراءة هذه السياسة قبل الاشتراك في
          أي من خدماتنا.
        </p>

        <!-- Cancellation and Refund -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          2. الإلغاء والاسترجاع
        </h2>
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
            إذا تم تقديم أي من الخدمات القانونية خلال فترة الإلغاء، لا يحق
            للعميل المطالبة برد المبلغ كاملاً، ويتم خصم قيمة الخدمات التي تم
            تقديمها بناءً على السعر المنفصل لكل خدمة.
          </li>
        </ul>

        <!-- Replacement -->
        <h2 class="text-xl font-semibold mb-4 text-center">3. الاستبدال</h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            يمكن للعميل طلب استبدال الباقة بخدمة أخرى أو ترقية/تخفيض الباقة خلال
            أول 30 يومًا من الاشتراك، على أن يتم تسوية الفروق المالية بين
            الباقات.
          </li>
          <li>
            في حالة استبدال الباقة، يتم حساب أي فروقات مالية، ويُطلب من العميل
            دفع الفارق (في حال الترقية)، أو استرداد الفارق (في حال التخفيض).
          </li>
        </ul>

        <!-- Non-Refundable Services -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          4. الخدمات غير القابلة للاسترجاع
        </h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            أي خدمات قانونية يتم تقديمها بشكل فوري مثل الاستشارات، إعداد الوثائق
            القانونية، أو تقديم المذكرات، لا تكون قابلة للاسترجاع أو الاستبدال
            بعد تقديم الخدمة.
          </li>
          <li>باقات الاشتراك المنتهية لا تكون قابلة للاسترجاع أو التمديد.</li>
        </ul>

        <!-- Return or Replacement Request Process -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          5. آلية طلب الإرجاع أو الاستبدال
        </h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            يجب تقديم طلب الإرجاع أو الاستبدال عبر البريد الإلكتروني الرسمي أو
            من خلال حساب العميل في الموقع.
          </li>
          <li>
            يتعين على العميل توضيح سبب طلب الإرجاع أو الاستبدال مع تقديم ما يثبت
            عدم الاستفادة من الخدمات (إن أمكن).
          </li>
        </ul>

        <!-- Processing Time -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          6. الوقت المستغرق لمعالجة الطلبات
        </h2>
        <p class="mb-4">
          يتم معالجة طلبات الإلغاء، الاسترجاع أو الاستبدال في غضون 10 أيام عمل
          من تاريخ استلام الطلب.
        </p>

        <!-- Exceptions -->
        <h2 class="text-xl font-semibold mb-4 text-center">7. استثناءات</h2>
        <p class="mb-4">
          تحتفظ الشركة بالحق في رفض أي طلب استرجاع أو استبدال في حالة وجود سوء
          استخدام أو خرق لشروط الخدمة من قبل العميل.
        </p>

        <!-- Policy Modifications -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          8. التعديلات على السياسة
        </h2>
        <p class="mb-4">
          تحتفظ الشركة بحق تعديل هذه السياسة في أي وقت، وسيتم إخطار العملاء بأي
          تغييرات جوهرية من خلال الموقع.
        </p>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">إغلاق</button>
        </form>
      </div>
    </div>
    <div class="modal-box" v-else>
      <div class="modal-action my-0 justify-start">
        <form method="dialog">
          <button class="btn">
            <font-awesome-icon icon="fa-solid fa-x" />
          </button>
        </form>
      </div>
      <h3 class="text-lg font-bold text-center pb-2">
        Return and Exchange Policy
      </h3>
      <div
        class="p-6 px-8 bg-white rounded-lg shadow-lg max-w-3xl mx-auto text-black"
      >
        <!-- Policy Scope -->
        <h2 class="text-xl font-semibold mb-4 text-center">1. Policy Scope</h2>
        <p class="mb-4">
          This policy applies to all legal services provided through the site
          under annual package subscriptions. Customers are required to read
          this policy before subscribing to any of our services.
        </p>

        <!-- Cancellation and Refund -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          2. Cancellation and Refund
        </h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            The customer may request to cancel their annual subscription within
            7 days from the date of the initial payment, provided no legal
            services included in the package have been utilized.
          </li>
          <li>
            If cancellation is requested during the grace period, the full
            amount paid will be refunded after deducting any administrative or
            banking fees.
          </li>
          <li>
            If any legal services were provided during the cancellation period,
            the customer is not entitled to a full refund, and the cost of the
            services provided will be deducted based on the separate price for
            each service.
          </li>
        </ul>

        <!-- Replacement -->
        <h2 class="text-xl font-semibold mb-4 text-center">3. Replacement</h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            The customer may request to replace their package with another
            service or upgrade/downgrade their package within the first 30 days
            of subscription, with any financial differences settled between the
            packages.
          </li>
          <li>
            In the case of package replacement, any financial differences will
            be calculated, and the customer will be required to pay the
            difference (in case of an upgrade) or receive a refund of the
            difference (in case of a downgrade).
          </li>
        </ul>

        <!-- Non-Refundable Services -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          4. Non-Refundable Services
        </h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            Any legal services provided immediately, such as consultations,
            preparation of legal documents, or submission of briefs, are not
            refundable or exchangeable after the service is rendered.
          </li>
          <li>
            Expired subscription packages are not refundable or extendable.
          </li>
        </ul>

        <!-- Return or Replacement Request Process -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          5. Return or Replacement Request Process
        </h2>
        <ul class="list-decimal pl-5 mb-4">
          <li>
            Requests for returns or replacements must be submitted via the
            official email or through the customer account on the site.
          </li>
          <li>
            The customer must clarify the reason for the return or replacement
            request and provide proof of non-utilization of services (if
            possible).
          </li>
        </ul>

        <!-- Processing Time -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          6. Processing Time
        </h2>
        <p class="mb-4">
          Cancellation, refund, or replacement requests will be processed within
          10 business days from the date of receipt of the request.
        </p>

        <!-- Exceptions -->
        <h2 class="text-xl font-semibold mb-4 text-center">7. Exceptions</h2>
        <p class="mb-4">
          The company reserves the right to refuse any return or replacement
          request in cases of misuse or violation of the terms of service by the
          customer.
        </p>

        <!-- Policy Modifications -->
        <h2 class="text-xl font-semibold mb-4 text-center">
          8. Policy Modifications
        </h2>
        <p class="mb-4">
          The company reserves the right to modify this policy at any time and
          will notify customers of any significant changes through the website.
        </p>
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn">Close</button>
        </form>
      </div>
    </div>
  </dialog>
</template>

<style scoped>
.navbar {
  direction: ltr;
}
.modal-box {
  position: relative;
}

.modal-box::before {
  content: "";
  position: absolute;
  z-index: -1;
  top: 50%;
  left: 50%;
  width: 50%;
  height: 50%;
  transform: translate(-50%, -50%);
  background-image: url("../assets/images/logo.png");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  opacity: 0.05;
}
.navbar {
  transform: translate3d(0, 0, 0);
  transition: all 0.2s ease-out;
}

.navbar_hidden {
  transform: translate3d(0, -100%, 0);
}
</style>

<script setup>
import { useI18n } from "vue-i18n";
const { t } = useI18n();
const { locale } = useI18n();
import { ref, reactive, onMounted, watch } from "vue";
import axios from "axios";
import showToastMessage from "../router/toastmessage";
import LanguageSelect from "./LanguageSelect.vue";

const selectedLanguage = ref("");
const saveLanguage = () => {
  localStorage.setItem("language", selectedLanguage.value);
};
const countries = ref([]);
const cities = ref([]);
const btnn = ref(null);
const allCities = [
  { arabic_name: "أبها", english_name: "Abha" },
  { arabic_name: "أبو عريش", english_name: "Abu Arish" },
  { arabic_name: "أحد المسارحة", english_name: "Ahad Al Masarihah" },
  { arabic_name: "أحد رفيدة", english_name: "Ahad Rufaida" },
  { arabic_name: "أضم", english_name: "Adham" },
  { arabic_name: "أملج", english_name: "Umluj" },
  { arabic_name: "الأحساء", english_name: "Al-Ahsa" },
  { arabic_name: "الأسياح", english_name: "Al Asyah" },
  { arabic_name: "الأفلاج", english_name: "Al Aflaj" },
  { arabic_name: "الباحة", english_name: "Al Bahah" },
  { arabic_name: "البدائع", english_name: "Al Badai" },
  { arabic_name: "البدع", english_name: "Al Bada'a" },
  { arabic_name: "البرك", english_name: "Al-Birk" },
  { arabic_name: "البكيرية", english_name: "Al Bukayriyah" },
  { arabic_name: "البيضاء", english_name: "Al Bayda" },
  { arabic_name: "الجبيل", english_name: "Al Jubail" },
  { arabic_name: "الجموم", english_name: "Al Jumum" },
  { arabic_name: "الحائط", english_name: "Al Hait" },
  { arabic_name: "الحجرة", english_name: "Al Hujrah" },
  { arabic_name: "الحرث", english_name: "Al Harath" },
  { arabic_name: "الحرجة", english_name: "Al Harajah" },
  { arabic_name: "الحريق", english_name: "Al Hariq" },
  { arabic_name: "الحناكية", english_name: "Al Hinakiyah" },
  { arabic_name: "الخبر", english_name: "Al Khobar" },
  { arabic_name: "الخرج", english_name: "Al Kharj" },
  { arabic_name: "الخرمة", english_name: "Al Khurma" },
  { arabic_name: "الخفجي", english_name: "Al Khafji" },
  { arabic_name: "الدائر", english_name: "Al Dair" },
  { arabic_name: "الدرب", english_name: "Al Darb" },
  { arabic_name: "الدرعية", english_name: "Diriyah" },
  { arabic_name: "الدلم", english_name: "Al Dilam" },
  { arabic_name: "الدمام", english_name: "Dammam" },
  { arabic_name: "الدوادمي", english_name: "Al Duwadimi" },
  { arabic_name: "الرس", english_name: "Al Rass" },
  { arabic_name: "الرياض", english_name: "Riyadh" },
  { arabic_name: "الريث", english_name: "Al Rayth" },
  { arabic_name: "الرين", english_name: "Al Rayan" },
  { arabic_name: "الزلفي", english_name: "Al Zulfi" },
  { arabic_name: "السليل", english_name: "Al Sulayyil" },
  { arabic_name: "السليمي", english_name: "Al Sulaymi" },
  { arabic_name: "الشماسية", english_name: "Al Shamasiyah" },
  { arabic_name: "الشملي", english_name: "Al Shumli" },
  { arabic_name: "الشنان", english_name: "Al Shinan" },
  { arabic_name: "الطائف", english_name: "Taif" },
  { arabic_name: "الطوال", english_name: "Al Tawwal" },
  { arabic_name: "العارضة", english_name: "Al Aridah" },
  { arabic_name: "العديد", english_name: "Al Udaid" },
  { arabic_name: "العرضيات", english_name: "Al Aridiyat" },
  { arabic_name: "العقيق", english_name: "Al Aqiq" },
  { arabic_name: "العلا", english_name: "Al Ula" },
  { arabic_name: "العويقيلة", english_name: "Al Uwaigilah" },
  { arabic_name: "العيدابي", english_name: "Al Aidabi" },
  { arabic_name: "العيص", english_name: "Al Ays" },
  { arabic_name: "الغاط", english_name: "Al Ghat" },
  { arabic_name: "الغزالة", english_name: "Al Ghazalah" },
  { arabic_name: "القرى", english_name: "Al Qura" },
  { arabic_name: "القريات", english_name: "Al Qurayyat" },
  { arabic_name: "القطيف", english_name: "Qatif" },
  { arabic_name: "القنفذة", english_name: "Al Qunfudhah" },
  { arabic_name: "القويعية", english_name: "Al Quwaiyah" },
  { arabic_name: "الكامل", english_name: "Al Kamil" },
  { arabic_name: "الليث", english_name: "Al Lith" },
  { arabic_name: "المجاردة", english_name: "Al Majaridah" },
  { arabic_name: "المجمعة", english_name: "Al Majma'ah" },
  { arabic_name: "المخواة", english_name: "Al Makhwah" },
  { arabic_name: "المدينة المنورة", english_name: "Medina" },
  { arabic_name: "المذنب", english_name: "Al Mithnab" },
  { arabic_name: "المزاحمية", english_name: "Al Muzahimiyah" },
  { arabic_name: "المملكة العربية السعودية", english_name: "Saudi Arabia" },
  { arabic_name: "المندق", english_name: "Al Mandak" },
  { arabic_name: "المنطقة الشرقية", english_name: "Eastern Province" },
  { arabic_name: "المهد", english_name: "Al Mahd" },
  { arabic_name: "الموية", english_name: "Al Muwayh" },
  { arabic_name: "النبهانية", english_name: "Al Nabhaniah" },
  { arabic_name: "النعيرية", english_name: "Al Nairyah" },
  { arabic_name: "النماص", english_name: "Al Namas" },
  { arabic_name: "الوجه", english_name: "Al Wajh" },
  { arabic_name: "بارق", english_name: "Bariq" },
  { arabic_name: "بحرة", english_name: "Bahrah" },
  { arabic_name: "بدر", english_name: "Badr" },
  { arabic_name: "بدر الجنوب", english_name: "Badr Al Janoub" },
  { arabic_name: "بريدة", english_name: "Buraidah" },
  { arabic_name: "بقعاء", english_name: "Baqa'a" },
  { arabic_name: "بقيق", english_name: "Buqayq" },
  { arabic_name: "بلجرشي", english_name: "Baljurashi" },
  { arabic_name: "بلقرن", english_name: "Balqarn" },
  { arabic_name: "بني حسن", english_name: "Bani Hassan" },
  { arabic_name: "بيش", english_name: "Bish" },
  { arabic_name: "بيشة", english_name: "Bisha" },
  { arabic_name: "تبوك", english_name: "Tabuk" },
  { arabic_name: "تثليث", english_name: "Tathlith" },
  { arabic_name: "تربة", english_name: "Turbah" },
  { arabic_name: "تنومة", english_name: "Tanomah" },
  { arabic_name: "تيماء", english_name: "Tayma" },
  { arabic_name: "ثادق", english_name: "Thadek" },
  { arabic_name: "ثار", english_name: "Thar" },
  { arabic_name: "جازان", english_name: "Jazan" },
  { arabic_name: "جدة", english_name: "Jeddah" },
  { arabic_name: "حائل", english_name: "Hail" },
  { arabic_name: "حبونا", english_name: "Habouna" },
  { arabic_name: "حريملاء", english_name: "Huraymila" },
  { arabic_name: "حفر الباطن", english_name: "Hafar Al-Batin" },
  { arabic_name: "حقل", english_name: "Haql" },
  { arabic_name: "حوطة بني تميم", english_name: "Howtat Bani Tamim" },
  { arabic_name: "خباش", english_name: "Khabbash" },
  { arabic_name: "خليص", english_name: "Khulais" },
  { arabic_name: "خميس مشيط", english_name: "Khamis Mushait" },
  { arabic_name: "خيبر", english_name: "Khaybar" },
  { arabic_name: "دومة الجندل", english_name: "Dumat Al-Jandal" },
  { arabic_name: "رأس تنورة", english_name: "Ras Tanura" },
  { arabic_name: "رابغ", english_name: "Rabigh" },
  { arabic_name: "رجال ألمع", english_name: "Rijal Almaa" },
  { arabic_name: "رفحاء", english_name: "Rafha" },
  { arabic_name: "رماح", english_name: "Rumah" },
  { arabic_name: "رنية", english_name: "Ranya" },
  { arabic_name: "رياض الخبراء", english_name: "Riyadh Al Khabra" },
  { arabic_name: "سراة عبيدة", english_name: "Sarat Abidah" },
  { arabic_name: "سكاكا", english_name: "Sakaka" },
  { arabic_name: "سميراء", english_name: "Samira" },
  { arabic_name: "شرورة", english_name: "Sharurah" },
  { arabic_name: "شقراء", english_name: "Shaqra" },
  { arabic_name: "صامطة", english_name: "Samtah" },
  { arabic_name: "صبيا", english_name: "Sabya" },
  { arabic_name: "ضباء", english_name: "Duba" },
  { arabic_name: "ضرما", english_name: "Durma" },
  { arabic_name: "ضرية", english_name: "Dariyah" },
  { arabic_name: "ضمد", english_name: "Damad" },
  { arabic_name: "طبرجل", english_name: "Tabarjal" },
  { arabic_name: "طريب", english_name: "Tareeb" },
  { arabic_name: "طريف", english_name: "Turayf" },
  { arabic_name: "ظهران الجنوب", english_name: "Dhahran Al Janoub" },
  { arabic_name: "عرعر", english_name: "Arar" },
  { arabic_name: "عفيف", english_name: "Afif" },
  { arabic_name: "عقلة الصقور", english_name: "Oqlat Al Suqoor" },
  { arabic_name: "عنيزة", english_name: "Unaizah" },
  { arabic_name: "عيون الجواء", english_name: "Oyoon Al Jwa" },
  { arabic_name: "غامد الزناد", english_name: "Ghamid Al-Zenad" },
  { arabic_name: "فرسان", english_name: "Farasan" },
  { arabic_name: "فيفاء", english_name: "Faifa" },
  { arabic_name: "قرية العليا", english_name: "Qaryat Al Ulya" },
  { arabic_name: "قلوة", english_name: "Qilwah" },
  { arabic_name: "كل الأقاليم", english_name: "All Regions" },
  { arabic_name: "محايل عسير", english_name: "Muhayil Asir" },
  { arabic_name: "مرات", english_name: "Marat" },
  { arabic_name: "مكة", english_name: "Makkah" },
  { arabic_name: "منطقة الباحة", english_name: "Al Bahah Region" },
  { arabic_name: "منطقة الجوف", english_name: "Al Jouf Region" },
  {
    arabic_name: "منطقة الحدود الشمالية",
    english_name: "Northern Borders Region",
  },
  { arabic_name: "منطقة الرياض", english_name: "Riyadh Region" },
  { arabic_name: "منطقة القصيم", english_name: "Al Qassim Region" },
  { arabic_name: "منطقة المدينة المنورة", english_name: "Al Madinah Region" },
  { arabic_name: "منطقة تبوك", english_name: "Tabuk Region" },
  { arabic_name: "منطقة جازان", english_name: "Jazan Region" },
  { arabic_name: "منطقة حائل", english_name: "Hail Region" },
  { arabic_name: "منطقة عسير", english_name: "Asir Region" },
  { arabic_name: "منطقة مكة المكرمة", english_name: "Makkah Region" },
  { arabic_name: "منطقة نجران", english_name: "Najran Region" },
  { arabic_name: "موقق", english_name: "Muwaqqaq" },
  { arabic_name: "ميسان", english_name: "Maysan" },
  { arabic_name: "نجران", english_name: "Najran" },
  { arabic_name: "هروب", english_name: "Haroub" },
  { arabic_name: "وادي الدواسر", english_name: "Wadi Al-Dawasir" },
  { arabic_name: "وادي الفرع", english_name: "Wadi Al Far'" },
  { arabic_name: "يدمة", english_name: "Yadamah" },
  { arabic_name: "ينبع", english_name: "Yanbu" },
];

// Toast Message
const toastMessage = ref(null);
const showToast = ref(false);

// Loading State
const loading = ref(false);

// Form Data
const form = ref({
  first_name: "",
  email: "",
  mobile_no: "",
  job_title: "",
  city: "",
  nationality: "",
  send_updates: true,
  accept_terms: true,
});

// Errors Object
const errors = reactive({
  first_name: null,
  email: null,
  mobile_no: null,
  job_title: null,
  city: null,
  nationality: null,
  general: null,
});

// Helper functions for validation
const isValidEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const isValidMobileNumber = (mobile_no) => {
  const mobileRegex = /^[0-9]{8,15}$/; // Adjust for your format
  return mobileRegex.test(mobile_no);
};

// Form Validation Function
const validateForm = () => {
  // Reset error messages
  errors.first_name = null;
  errors.email = null;
  errors.mobile_no = null;
  errors.city = null;
  errors.job_title = null;
  errors.nationality = null;
  // errors.accept_terms = null;

  if (locale.value === "ar") {
    errors.first_name = form.value.first_name ? null : "يرجى إدخال الاسم.";
    errors.email = form.value.email
      ? isValidEmail(form.value.email)
        ? null
        : "يرجى إدخال بريد إلكتروني صحيح مثال: example@gmail.com"
      : "يرجى إدخال البريد الإلكتروني.";
    errors.mobile_no = form.value.mobile_no
      ? isValidMobileNumber(form.value.mobile_no)
        ? null
        : "يرجى إدخال رقم هاتف صالح."
      : "يرجى إدخال رقم هاتف.";
    errors.city = form.value.city ? null : "يرجى إدخال المدينة.";
    errors.job_title = form.value.job_title ? null : "يرجى إدخال الوظيفة.";
    errors.nationality = form.value.nationality ? null : "يرجى إدخال الجنسية.";
    // errors.accept_terms = form.value.accept_terms
    //   ? null
    //   : "يجب الموافقة على شروط الاستخدام.";
  } else {
    errors.first_name = form.value.first_name
      ? null
      : "Please enter your name.";
    errors.email = form.value.email
      ? isValidEmail(form.value.email)
        ? null
        : "Please enter a valid email. example@gmail.com"
      : "Please enter your email.";
    errors.mobile_no = form.value.mobile_no
      ? isValidMobileNumber(form.value.mobile_no)
        ? null
        : "Please enter a valid mobile number."
      : "Please enter your mobile number.";
    errors.city = form.value.city ? null : "Please enter your city.";
    errors.job_title = form.value.job_title
      ? null
      : "Please enter your job title.";
    errors.nationality = form.value.nationality
      ? null
      : "Please enter your nationality.";
    // errors.accept_terms = form.value.accept_terms
    //   ? null
    //   : "You must accept the terms of use.";
  }

  // Return true if no errors exist
  return (
    !errors.first_name &&
    !errors.email &&
    !errors.mobile_no &&
    !errors.city &&
    !errors.job_title &&
    !errors.nationality
    // !errors.accept_terms
  );
};

function fetchCountries() {
  fetch(
    `/api/method/lsc_api.lsc_api.get_linked_data.get_countries?lang=${
      locale.value || "ar"
    }`,
    { method: "GET" }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch countries.");
      }
      return response.json();
    })
    .then((data) => {
      countries.value = data.message.nationality;
    })
    .catch((error) => {
      console.error("Error fetching countries:", error);
    });
}
function fetchCities() {
  fetch(
    `/api/method/lsc_api.lsc_api.get_linked_data.get_work_cities?lang=${
      locale.value || "ar"
    }`,
    { method: "GET" }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch countries.");
      }
      return response.json();
    })
    .then((data) => {
      cities.value = data.message.work_city;
    })
    .catch((error) => {
      console.error("Error fetching countries:", error);
    });
}

onMounted(() => {
  fetchCountries();
  fetchCities();
});

watch(locale, () => {
  fetchCountries();
  fetchCities();
});

// Handle Form Submission
const handleSubmit = async () => {
  if (!validateForm()) return;

  loading.value = true;

  try {
    const response = await axios.post(
      "/api/method/lsc_api.lsc_api.create_lead.create_lead",
      { data: form.value },
      {
        withCredentials: true,
      }
    );

    if (locale.value === "ar") {
      if (response.data.message.status !== "fail") {
        showToastMessage(
          "تم تسجيل بنجاح، سيتم التواصل معك قريباً.",
          toastMessage,
          showToast
        );
        loading.value = false;
      } else {
        showToastMessage(
          "خطأ: الاسم او الايميل مسجل مسبقاً",
          toastMessage,
          showToast
        );
        loading.value = false;
      }
    } else {
      if (response.data.message.status !== "fail") {
        showToastMessage("Registered Successfully!", toastMessage, showToast);
        loading.value = false;
      } else {
        showToastMessage(
          "Failed: Name or Email is already used.",
          toastMessage,
          showToast
        );
        loading.value = false;
      }
    }
  } catch (error) {
    if (error.request.status == "409") {
      if (locale.value === "ar") {
        showToastMessage(
          "خطأ: الاسم او الايميل مسجل مسبقاً",
          toastMessage,
          showToast
        );
        loading.value = false;
      } else {
        showToastMessage(
          "Failed: Name or Email is already used.",
          toastMessage,
          showToast
        );
        loading.value = false;
      }
    }
  }
};
</script>
