<template>
  <div class="notification grid grid-cols-1 grid-rows-1 mt-44">
    <div
      v-for="notification in notifications"
      :key="notification.name"
      class="bg-white border-solid border-1 border-gray-200 flex items-center gap-3 p-5"
    >
      <div class="icon">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 448 512"
          width="18"
          height="18"
        >
          <path
            d="M224 0c-17.7 0-32 14.3-32 32l0 19.2C119 66 64 130.6 64 208l0 25.4c0 45.4-15.5 89.5-43.8 124.9L5.3 377c-5.8 7.2-6.9 17.1-2.9 25.4S14.8 416 24 416l400 0c9.2 0 17.6-5.3 21.6-13.6s2.9-18.2-2.9-25.4l-14.9-18.6C399.5 322.9 384 278.8 384 233.4l0-25.4c0-77.4-55-142-128-156.8L256 32c0-17.7-14.3-32-32-32zm0 96c61.9 0 112 50.1 112 112l0 25.4c0 47.9 13.9 94.6 39.7 134.6L72.3 368C98.1 328 112 281.3 112 233.4l0-25.4c0-61.9 50.1-112 112-112zm64 352l-64 0-64 0c0 17 6.7 33.3 18.7 45.3s28.3 18.7 45.3 18.7s33.3-6.7 45.3-18.7s18.7-28.3 18.7-45.3z"
          />
        </svg>
      </div>
      <div class="content text-right text-sm flex flex-col gap-2">
        <h4 class="text-black" v-html="notification.subject"></h4>
        <p>{{ notification.creation }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>

<script setup>
import { ref, onMounted } from "vue";

// test data to make it work dynamic please remove this variable and the line 142
const data = {
    "message": [
        {
            "name": "19mucfsian",
            "subject": "Failed to send email with subject: Welcome to LSC",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "12piifu70f",
            "creation": "2024-08-07 12:52:35.012393"
        },
        {
            "name": "0chcggpbcl",
            "subject": "<strong>Suha</strong> شارك مستند <strong>معاملات العملاء</strong> <b class=\"subject-title\">سهى الجهني-0414</b> معك",
            "type": "Share",
            "document_type": "Client Transactions",
            "document_name": "سهى الجهني-0414",
            "creation": "2024-08-01 10:24:39.475256"
        },
        {
            "name": "0c8gre2tma",
            "subject": "<strong>Suha</strong> شارك مستند <strong>معاملات العملاء</strong> <b class=\"subject-title\">سهى الجهني-0414</b> معك",
            "type": "Share",
            "document_type": "Client Transactions",
            "document_name": "سهى الجهني-0414",
            "creation": "2024-08-01 10:24:11.071536"
        },
        {
            "name": "17cke14g6e",
            "subject": "<strong>Suha</strong> ذكرتك في تعليق في <strong>Branch</strong> <b class=\"subject-title\">الرياض</b>",
            "type": "Mention",
            "document_type": "Branch",
            "document_name": "الرياض",
            "creation": "2024-06-05 10:12:01.946304"
        },
        {
            "name": "hmqtt0ofgd",
            "subject": "Failed to send email with subject: Mohamed Aglan خصص مهمة جديدة مبادرة البيع Ahmed لك",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "hf4ad5g2ep",
            "creation": "2024-05-23 16:48:18.906629"
        },
        {
            "name": "g0sn5p8jvj",
            "subject": "Failed to send email with subject: Mohamed Aglan خصص مهمة جديدة مبادرة البيع مصطفي عجلان لك",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "fovu5b2cd8",
            "creation": "2024-05-23 15:16:15.104070"
        },
        {
            "name": "gj85dibrkt",
            "subject": "Failed to send email with subject: Welcome to LSC",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "gclnapdduq",
            "creation": "2024-05-06 16:00:48.565124"
        },
        {
            "name": "p926q0ar30",
            "subject": "Failed to send email with subject: Welcome to LSC",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "p49u3cbf11",
            "creation": "2024-04-30 22:16:48.645788"
        },
        {
            "name": "d03dac41ad",
            "subject": "Failed to send email with subject: Mohamed Aglan خصص مهمة جديدة تقرير KSA VAT لك",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "72b6eba914",
            "creation": "2024-04-28 21:20:47.763344"
        },
        {
            "name": "4a7e4027fc",
            "subject": "Failed to send email with subject: Mohamed Aglan خصص مهمة جديدة حدث مقابلة لك",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "7a6893a0a2",
            "creation": "2024-04-25 00:32:06.196716"
        },
        {
            "name": "c99250830f",
            "subject": "Failed to send email with subject: File backup is ready",
            "type": "Alert",
            "document_type": "Email Queue",
            "document_name": "949b4793bb",
            "creation": "2024-04-22 23:16:14.976976"
        }
    ]
}
const notifications = ref([]);

const getNotificationsData = async () => {
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_user_notifications.get_user_notifications"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    notifications.value = data.message;
  } catch (error) {
    console.error("Error fetching user data:", error);
  }

  notifications.value = data.message
};
onMounted(() => {
  getNotificationsData();
});
</script>
