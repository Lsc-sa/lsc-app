<template>
  <section
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    id="contact"
    class="contact w-full px-4 min-h-screen lg:min-h-full 3xl:min-h-screen flex flex-col justify-center"
  >
    <SectionTitle :title="t('Contact')" />

    <div
      class="flex lg:w-4/5 mx-auto flex-col gap-2 lg:flex-row w-full lg:gap-6"
    >
      <div
        class="contact-form my-4 py-4 px-8 flex flex-col lg:flex-grow shadow-sm bg-white rounded-2xl"
      >
        <div class="cont-info flex flex-col lg:flex-row lg:gap-4 w-full">
          <label class="form-control w-full">
            <div class="label">
              <span class="label-text">
                {{ $t("ContactSection.name") }}
              </span>
            </div>
            <input
              type="text"
              :placeholder="t('ContactSection.namePlaceholder')"
              class="input input-bordered w-full"
            />
          </label>
          <label class="form-control w-full">
            <div class="label">
              <span class="label-text">
                {{ $t("ContactSection.email") }}
              </span>
            </div>
            <input
              type="text"
              :placeholder="t('ContactSection.emailPlaceholder')"
              class="input input-bordered w-full"
            />
          </label>
        </div>
        <label class="form-control w-full">
          <div class="label">
            <span class="label-text">
              {{ $t("ContactSection.subject") }}
            </span>
          </div>
          <input
            type="text"
            :placeholder="t('ContactSection.subjectPlaceholder')"
            class="input input-bordered w-full"
          />
        </label>
        <label class="form-control">
          <div class="label">
            <span class="label-text">
              {{ $t("ContactSection.message") }}
            </span>
            <!-- <span class="label-text-alt">0 / 400</span> -->
          </div>
          <textarea
            class="textarea textarea-bordered h-32 mb-4"
            :placeholder="t('ContactSection.msgbody')"
          ></textarea>
        </label>
        <button class="btn btn-primary">
          {{ $t("ContactSection.sendMessageButton") }}
        </button>
      </div>
      <div class="contact-map my-4 w-full flex-grow lg:w-1/2 shadow-sm">
        <div class="map-info h-80 lg:h-full border rounded-xl border-gray-600">
          <!-- <iframe
            class="w-full h-full rounded-xl"
            src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3623.22883130843!2d46.74059132536743!3d24.7533421279994!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e2f0396266fd2ed%3A0xaacee2ad0e3cb1d6!2sTakamul%20Law%20Firm%20and%20Legal%20Consultations!5e0!3m2!1sen!2seg!4v1724780180794!5m2!1sen!2seg"
            style="border: 0"
            allowfullscreen=""
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe> -->
          <img
            src="../assets/images/contact.jpg"
            alt="contact"
            class="w-full h-full rounded-xl"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.label-text {
  color: black;
}
.input,
.textarea {
  background-color: #fff;
}
</style>

<script setup>
import SectionTitle from "./SectionTitle.vue";
import { useI18n } from "vue-i18n";
const { t } = useI18n();
</script>
