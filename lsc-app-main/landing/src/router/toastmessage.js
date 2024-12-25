
const showToastMessage = (message,toastMessage ,showToast) => {
    toastMessage.value = message;
    showToast.value = true;
    setTimeout(() => {
      showToast.value = false;
    }, 3000); // Toast disappears after 3 seconds
  };
  
export default showToastMessage;