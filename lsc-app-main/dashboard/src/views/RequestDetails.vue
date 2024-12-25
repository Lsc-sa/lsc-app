<template>
  <LoggedInTopNav :title="t('Request Status')" :backArrow="true" />
  <div
    :dir="$i18n.locale == 'ar' ? 'rtl' : 'ltr'"
    class="flex items-center justify-center mt-24 lg:mt-40 sm:mt-32 mb-16 pb-16"
  >
    <div
      ref="chatContainer"
      class="chat-container chatContainer flex flex-col w-full gap-4 p-8 mx-0 rounded-box"
    >
      <div v-if="requestStatus != null">
        <p class="text-xs text-gray-500 text-center">
          {{ $t("Request created on") }}
          :
          <br />
          {{ formatTimestampTo12Hour(requestStatus.creation) }}
        </p>
        <div class="flex flex-row items-start">
          <div
            class="icon bg-white w-11 h-8 flex justify-center items-center rounded-full p-0 m-0"
          >
            <img
              src="../assets/images/logo.png"
              width="16"
              height="16"
              alt="system-message"
            />
          </div>
          <div class="bg-white p-4 mx-3 rounded-lg shadow w-full">
            <p v-if="requestStatus.name" class="text-gray-500">
              {{ $t("Request No.") }}
              :
              {{ requestStatus.name.split("-")[1] }}
            </p>
            <p class="text-gray-500">
              {{ $t("Request Status") }}
              :
              {{ requestStatus.status }}
            </p>
            <p class="text-gray-500">
              {{ $t("Service type") }}
              :
              {{ requestStatus.item }}
            </p>
            <p class="text-gray-500">
              {{ $t("Details") }}
              :
              {{ requestStatus.description }}
            </p>
          </div>
        </div>
      </div>
      <div
        v-if="comments"
        class="message flex flex-col gap-1"
        v-for="(comment, index) in filteredComments"
        :key="`${comment.content} ${index}`"
      >
        <span class="text-xs text-gray-500 text-center">
          {{ formatTimestampTo12Hour(comment.creation) }}
        </span>
        <div
          class="flex flex-row items-start"
          v-if="comment.comment_type == 'Comment'"
        >
          <div
            class="icon bg-white w-11 h-8 flex justify-center items-center rounded-full p-0 m-0"
            v-if="usermail != comment.owner"
          >
            <img
              src="../assets/images/logo.png"
              width="16"
              height="16"
              alt="system-message"
            />
          </div>
          <div
            class="icon bg-white w-11 h-8 flex justify-center items-center rounded-full p-0 m-0 order-1"
            v-else
          >
            <img
              v-if="userData.user_image"
              :src="userData.user_image"
              style="
                width: 40px;
                border-radius: 50%;
                height: 40px;
                object-fit: contain;
              "
              alt="my-message"
            />
            <font-awesome-icon
              v-else
              icon="fa-regular fa-user"
              class="w-4 h-4 text-black"
            />
          </div>
          <div
            class="bg-white p-4 mx-3 rounded-lg shadow w-full"
            v-if="comment?.content?.includes(' || ')"
          >
            <h4 class="text-primary">
              {{
                parseHTML(comment.content)?.split(" || ")[0]?.split("label:")[1]
              }}
            </h4>
            <div class="btns flex flex-row justify-center items-center gap-2">
              <a
                class="btn btn-secondry btn-sm bg-primary border-none hover:bg-primary text-white"
                :href="
                  parseHTML(comment.content)
                    ?.split(' || ')[2]
                    ?.split('link:')[1]
                "
                :target="
                  (() => {
                    const tabValue = parseHTML(comment.content)
                      ?.split(' || ')[1]
                      ?.split('tab:')[1];
                    return tabValue == 0 ? '_self' : '_blank';
                  })()
                "
              >
                {{ $t("Show") }}
              </a>
            </div>
            <!-- <div class="btns flex flex-row justify-center items-center gap-2">
              <a
                class="btn btn-secondry btn-sm bg-primary border-none hover:bg-primary text-white"
                :href="
                  parseHTML(comment.content)
                    ?.split(' || ')[2]
                    ?.split('link:')[1]
                "
                :target="
                  (() => {
                    const tabValue = parseHTML(comment.content)
                      ?.split(' || ')[1]
                      ?.split('tab:')[1];
                    return tabValue == 1 ? '_self' : '_blank';
                  })()
                "
                download
              >
                {{ $t("Download") }}
              </a>
            </div> -->
          </div>
          <div class="bg-white p-4 mx-3 rounded-lg shadow w-full" v-else>
            <p class="text-black">{{ parseHTML(comment.content) }}</p>
          </div>
        </div>
        <div
          class="bg-primaryMoreLight p-5 mx-16 mt-4 rounded-lg shadow flex flex-col justify-center items-center gap-2"
          v-else-if="comment.comment_type == 'Attachment'"
        >
          <h4 class="text-primary">
            {{ $t("File Attached") }}
          </h4>
          <div class="btns flex flex-row justify-center items-center gap-2">
            <a
              class="btn btn-secondry btn-sm bg-primary border-none hover:bg-primary text-white"
              :href="getHrefFromContent(comment.content)"
              target="_blank"
            >
              {{ $t("Show") }}
            </a>
            <!-- <div class="btns flex flex-row justify-center items-center gap-2">
              <a
                class="btn btn-secondry btn-sm bg-primary border-none hover:bg-primary text-white"
                :href="getHrefFromContent(comment.content)"
                target="_blank"
                download
              >
                {{ $t("Download") }}
              </a>
            </div> -->
          </div>
          <div
            class="icon bg-white w-11 h-8 flex justify-center items-center rounded-full p-0 m-0"
            v-if="usermail != comment.owner"
          >
            <img
              src="../assets/images/logo.png"
              width="16"
              height="16"
              alt="system-message"
            />
          </div>
          <div
            class="icon bg-white w-11 h-8 flex justify-center items-center rounded-full p-0 m-0 order-1"
            v-else
          >
            <img
              v-if="userData.user_image"
              :src="userData.user_image"
              style="
                width: 40px;
                border-radius: 50%;
                height: 40px;
                object-fit: contain;
              "
              alt="my-message"
            />
            <font-awesome-icon
              v-else
              icon="fa-regular fa-user"
              class="w-4 h-4 text-black"
            />
          </div>
        </div>
      </div>
      <div
        v-if="isUploading"
        class="bg-primaryMoreLight p-5 mx-16 mt-4 rounded-lg shadow flex flex-col justify-center items-center gap-2"
      >
        <h4 class="text-primary">
          {{ $t("Attaching File...") }}
        </h4>
        <div class="btns flex flex-row justify-center items-center gap-2">
          <font-awesome-icon
            icon="fa-solid fa-spinner"
            spin
            class="p-4 w-4 h-4 mx-2 bg-black text-white rounded-full"
          />
        </div>
      </div>
      <div
        class="flex flex-col items-center justify-center gap-4"
        v-if="!allowComments"
        style="direction: ltr"
      >
        <StarRating
          :increment="0.5"
          v-model:rating="selectedRating"
          :star-size="32"
          animate="true"
          rounded-corners="true"
          :read-only="rated"
        />
        <textarea
          v-model="feedback"
          :class="[
            'textarea textarea-bordered bg-white h-24 w-full disabled:bg-white text-black disabled:text-black',
            $i18n.locale == 'ar' ? 'text-right' : '',
          ]"
          :placeholder="t('Feedback')"
          :disabled="rated"
        ></textarea>
        <button
          v-if="!rated"
          class="btn btn-primary text-white border-white bg-primary w-full"
          @click="handleRateSubmit"
        >
          {{ t("Send") }}
        </button>
      </div>
    </div>
  </div>
  <form v-if="allowComments" @submit.prevent="handleSubmit">
    <div class="relative">
      <div
        class="chat-inputs flex justify-between fixed bottom-0 left-0 right-0 bg-white p-4"
      >
        <font-awesome-icon
          v-if="!changeIcon && !isUploading"
          icon="fa-solid fa-paperclip"
          :class="['p-4 w-4 h-4 mx-2 bg-black text-white rounded-full']"
          @click="triggerFileInput"
        />
        <font-awesome-icon
          v-else-if="isUploading"
          icon="fa-solid fa-spinner"
          spin
          class="p-4 w-4 h-4 mx-2 bg-black text-white rounded-full"
        />
        <font-awesome-icon
          v-else
          icon="fa-solid fa-circle-check"
          class="p-4 w-4 h-4 mx-2 bg-black text-primary rounded-full"
        />

        <!-- Hidden File Input -->
        <input
          type="file"
          ref="fileInput"
          class="hidden"
          accept="image/*,video/*,audio/*,.pdf,.doc,.docx"
          @change="handleFileChange"
        />
        <font-awesome-icon
          icon="fa-solid fa-paper-plane"
          @click="addComment"
          :class="[
            'p-4 w-4 h-4 mx-2 bg-black text-white rounded-full',
            isUploading ? '!text-red-800' : '',
          ]"
        />
        <input
          type="text"
          class="input input-bordered bg-gray-100 w-full text-black disabled:bg-gray-200 disabled:border-gray-200 disabled:text-black"
          :placeholder="t('Write a Message')"
          v-model="userComment"
        />
      </div>
    </div>
  </form>
  <div v-if="showToast" class="relative">
    <div class="toast bottom-20 left-1/2 -translate-x-1/2">
      <div class="alert alert-info bg-white border-2 border-primary">
        <span>{{ toastMessage }}</span>
      </div>
    </div>
  </div>
  <Loader v-if="loading" />
</template>

<script setup>
import { useI18n } from "vue-i18n";
const { t, locale } = useI18n();
import showToastMessage from "../router/toastmessage";
import Loader from "@/components/Loader.vue";
// import BottomNav from "@/components/BottomNav.vue";
import LoggedInTopNav from "../components/LoggedInTopNav.vue";
import { useRouter, useRoute } from "vue-router";
import {
  ref,
  onMounted,
  onUnmounted,
  computed,
  nextTick,
  watch,
  inject,
} from "vue";
import axios from "axios";
// import Vue3StarRatings from "vue3-star-ratings";
import StarRating from "vue-star-rating";
const showToast = ref(false);
const toastMessage = ref(null);

const selectedRating = ref(5);
const feedback = ref("");
const rated = ref(true);

async function handleRateSubmit() {
  loading.value = true;
  const response = await axios.post(
    "/api/method/lsc_api.lsc_api.client_rating.set_client_rating",
    {
      name: request_id,
      rating: selectedRating.value / 5,
      feedback: feedback.value,
    },
    {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    }
  );
  if (response.data.message.status == "success") {
    showToastMessage(t("Thank you!"), toastMessage, showToast);
    rated.value = true;
  } else {
    showToastMessage(
      t("Failed to rate, try again later."),
      toastMessage,
      showToast
    );
  }
  loading.value = false;
}
async function getRate() {
  loading.value = true;
  const response = await axios.get(
    "/api/method/lsc_api.lsc_api.client_rating.get_client_rating",
    { params: { name: request_id } },
    {
      headers: {
        "Content-Type": "application/json",
      },
      withCredentials: true,
    }
  );
  if (response.data.message.rating != 0) {
    rated.value = true;
    feedback.value = response.data.message.feedback;
    selectedRating.value = response.data.message.rating * 5;
  } else {
    rated.value = false;
  }
  loading.value = false;
}

const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
    window.scrollTo(
      {
        behavior: "smooth",
      },
      chatContainer.value.scrollHeight + 100
    );
  }
};
const fileInput = ref(null);
const changeIcon = ref(false);

const triggerFileInput = () => {
  fileInput.value.click();
};

// Router and navigation
const usermail = ref("");
const userComment = ref("");
const loading = ref(false);
const route = useRoute(); // Initialize useRoute to access route parameters
const request_id = route.query.requestId; // Extract requestId from route query
const isUploading = ref(false);
const navigate = useRouter();
const comments = ref(null);
const requestStatus = ref(null);
const allowComments = ref(true);
function allowNewComments() {
  if (
    requestStatus?.value?.status == "Done" ||
    requestStatus?.value?.status == "Refund" ||
    requestStatus?.value?.status == "Cancelled" ||
    requestStatus?.value?.status == "ألغيت" ||
    requestStatus?.value?.status == "مسترجعة" ||
    requestStatus?.value?.status == "تمت"
  ) {
    allowComments.value = false;
  }
}
// Request options for fetching logged-in user
const requestOptions = {
  method: "GET",
  headers: { Cookie: document.cookie },
  redirect: "follow",
};

function parseHTML(htmlString) {
  const parser = new DOMParser();
  const doc = parser.parseFromString(htmlString, "text/html");
  return doc.body.textContent || "";
}
const getHrefFromContent = (content) => {
  const tempDiv = document.createElement("div");
  tempDiv.innerHTML = content;
  const anchorTag = tempDiv.querySelector("a");
  return anchorTag ? anchorTag.getAttribute("href") : "";
};

const filteredComments = computed(() => {
  return comments.value.filter((comment) => {
    if (comment.comment_type === "Comment") {
      return true;
    }

    if (comment.comment_type === "Attachment") {
      const tempDiv = document.createElement("div");
      tempDiv.innerHTML = comment.content;
      const anchor = tempDiv.querySelector("a");
      const fileName = anchor ? anchor.textContent.trim() : "";

      const isRemoved = comments.value.some((delComment) => {
        return (
          delComment.comment_type === "Attachment Removed" &&
          delComment.content.includes(fileName)
        );
      });

      return !isRemoved;
    }

    return false;
  });
});
const chatContainer = ref(null);

const isCurrent = ref(true);
const fetchRequests = async () => {
  loading.value = true;
  try {
    const response = await axios.get(
      "/api/method/lsc_api.lsc_api.get_current_requests.get_current_requests"
    );
    if (response.data.message.requests) {
      loading.value = false;
      response.data.message.requests.filter((ele) => {
        if (ele.name === request_id) {
          requestStatus.value = {
            name: ele.name,
            status: ele.status,
            item: ele.item,
            creation: ele.creation,
            description: ele.description,
          };
          nextTick(() => {
            scrollToBottom();
            allowNewComments();
          });
          return (comments.value = ele?.comments?.reverse());
        } else {
          isCurrent.value = false;
        }
      });
    }
  } catch (error) {
    loading.value = false;
    console.error("Failed to fetch requests:", error);
  }
  if (!isCurrent.value) {
    try {
      const response = await axios.get(
        "/api/method/lsc_api.lsc_api.get_previous_requests.get_previous_requests"
      );
      if (response.data.message.requests) {
        loading.value = false;
        response.data.message.requests.filter((ele) => {
          if (ele.name === request_id) {
            requestStatus.value = {
              name: ele.name,
              status: ele.status,
              item: ele.item,
              creation: ele.creation,
              description: ele.description,
            };
            nextTick(() => {
              scrollToBottom();
              allowNewComments();
            });
            return (comments.value = ele?.comments?.reverse());
          } else {
            isCurrent.value = false;
          }
        });
      }
    } catch (error) {
      loading.value = false;
      console.error("Failed to fetch requests:", error);
    }
  }
};

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    changeIcon.value = true; // Change icon once file is selected
  }
};

const MAX_FILE_SIZE = 50 * 1024 * 1024; // 50MB in bytes

const addComment = async () => {
  if (!userComment.value && !changeIcon.value) return;
  if (isUploading.value) return;
  // loading.value = true;
  if (userComment.value) {
    const comment = userComment.value;
    userComment.value = "";
    try {
      // Post the comment content
      const response = await axios.post(
        "/api/method/lsc_api.lsc_api.create_comment.create_comment",
        { client_transaction: request_id, comment_content: comment },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true,
        }
      );
      nextTick(() => {
        scrollToBottom();
      });
    } catch (error) {
      loading.value = false;
      return;
    } finally {
      userComment.value = "";
    }
  }
  // Check if a file has been selected for upload
  if (fileInput.value && fileInput.value.files.length > 0) {
    const file = fileInput.value.files[0];
    if (file.size > MAX_FILE_SIZE) {
      showToastMessage(
        t("File size exceeds 50MB. Please upload a smaller file."),
        toastMessage,
        showToast
      );
      changeIcon.value = false;
      fileInput.value.value = ""; // Clear the file input
      return;
    }
    const formData = new FormData();
    formData.append("client_transaction", request_id);
    formData.append("file", file); // Append the file object itself

    try {
      localStorage.setItem(`uploading ${request_id}`, request_id);
      fileInput.value.value = ""; // Reset the file input field
      isUploading.value = true;
      const fileResponse = await axios.post(
        "/api/method/lsc_api.lsc_api.attach_file.attach_file",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data", // Set to multipart/form-data
          },
          withCredentials: true,
        }
      );
    } catch (fileError) {
      console.error("Failed to upload file:", fileError);
      if (fileError.response.status == "504") {
        showToastMessage(
          t("Network error, please check your internet connection."),
          toastMessage,
          showToast
        );
      }
    } finally {
      isUploading.value = false;
      localStorage.removeItem(`uploading ${request_id}`);
    }
  }
  nextTick(() => {
    scrollToBottom();
  });
  loading.value = false;
  userComment.value = "";
  fileInput.value.value = ""; // Reset the file input field
  changeIcon.value = false; // Reset the icon state

  // fetchRequests(); // Refresh the comments list
};
function formatTimestampTo12Hour(timestamp) {
  // Create a new Date object from the timestamp string
  const date = new Date(timestamp);

  let ampm;
  let dayName;
  // Get the name of the day (e.g., Monday, Tuesday, etc.)
  if (locale.value == "en") {
    dayName = date.toLocaleDateString("en", { weekday: "short" });
  } else {
    dayName = date.toLocaleDateString("ar-EG", { weekday: "short" });
  }

  // Extract parts of the date
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0"); // Months are zero-indexed
  const day = String(date.getDate()).padStart(2, "0");

  // Format hours and minutes
  let hours = date.getHours();
  const minutes = String(date.getMinutes()).padStart(2, "0");
  if (locale.value == "en") {
    ampm = hours >= 12 ? "PM" : "AM";
  } else {
    ampm = hours >= 12 ? "مساءاً" : "صباحاً";
  }
  hours = hours % 12 || 12; // Convert 24h to 12h format

  // Return the formatted date string with the day name
  return `${hours}:${minutes} ${ampm} -- ${dayName}، ${day}-${month}-${year}`;
}

const userData = ref({
  user_image: null,
});

const getUserData = async () => {
  isUploading.value =
    localStorage.getItem(`uploading ${request_id}`) == request_id
      ? true
      : false;
  try {
    const response = await fetch(
      "/api/method/lsc_api.lsc_api.get_user_data.get_user_data"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    userData.value = data.message.user_data;
  } catch (error) {
    console.error("Error fetching user data:", error);
  }
};
watch(comments, () => {
  nextTick(() => {
    scrollToBottom();
  });
});

// Fetch logged-in user on mount
const socket = inject("$socket");
if (!socket.hasDisconnectListener) {
  socket.on("disconnect", () => {
    console.log("Disconnected");
  });
  socket.hasDisconnectListener = true; // Track that the disconnect listener is set
}

onMounted(() => {
  getUserData();
  allowNewComments();
  fetchRequests();
  getRate();
  fetch("/api/method/frappe.auth.get_logged_user", requestOptions)
    .then((response) => response.json())
    .then((data) => (usermail.value = data.message))
    .catch(() => navigate.replace("/"));
  if (!socket.connected) {
    socket.connect();
  }
  const handleConnect = () => {
    console.log("Connected");
  };
  const handleNotificationData = (data) => {
    console.log(data);
  };

  socket.on("connect", handleConnect);
  socket.on(request_id, (data) => {
    if (data.comment_type == "Attachment") {
      loading.value = true;
      setTimeout(() => {
        fetchRequests();
        loading.value = false;
      }, 250);
    } else {
      comments.value.push(data);
      nextTick(() => {
        scrollToBottom();
      });
    }
  });
});

onUnmounted(() => {
  // Properly remove the specific listeners and disconnect the socket
  socket.off("connect");
  socket.off(request_id);
  socket.disconnect();
});
</script>

<style scoped>
.chat-container {
  margin: 0 auto;
  background-color: rgb(242 242 242);
}

.message {
  width: 100%;
}

::v-deep(.vue-star-rating) {
  position: relative;
}
::v-deep(.sr-only) {
  left: 0 !important;
}
</style>
