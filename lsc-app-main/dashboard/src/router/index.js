import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import SignupView from "../views/SignupView.vue";
import PersonalinfoView from "../views/PersonalinfoView.vue";
import ResidentialinfoView from "../views/ResidentialinfoView.vue";
import AllInvoicesView from "../views/AllInvoicesView.vue";
import PaymentResponseView from "../views/PaymentResponseView.vue";
import NProfileView from "../views/NProfileView.vue";
import UserHome from "../views/UserHome.vue";
import RequestsView from "../views/RequestsView.vue";
import ServicesView from "../views/ServicesView.vue";
import PackagesView from "../views/PackagesView.vue";
import Paynow from "../views/Paynow.vue";
import Loading from "../views/Loading.vue";
import NotificationsView from "../views/NotificationsView.vue";
import StudyCaseView from "../views/StudyCaseView.vue";
import CreateCaseView from "../views/CreateCaseView.vue";
import CreateConsultationView from "../views/CreateConsultationView.vue";
import LegalServiceView from "../views/LegalServiceView.vue";
import RequestFollowUp from "../views/RequestFollowUp.vue";
import RequestDetails from "../views/RequestDetails.vue";
import UserSettingsView from "../views/UserSettingsView.vue";
import PowerofAttView from "../views/PowerofAttView.vue";
import PrivacyPolicy from "../views/PrivacyPolicy.vue";
import ContactUs from "../views/ContactUs.vue";
import InquiriesPolicy from "../views/InquiriesPolicy.vue";
import AccountStatusPage from "../views/AccountStatusPage.vue";
import ReturnPolicy from "../views/ReturnPolicy.vue";
import TermsView from "../views/TermsView.vue";
import CurrentPackageView from "../views/CurrentPackageView.vue";
import AnewPrint from "../views/AnewPrint.vue";
import ForgetPassword from "../views/ForgetPassword.vue";

const router = createRouter({
  base: "/dashboard/",
  history: createWebHistory("/dashboard"),
  routes: [
    {
      path: "/",
      name: "login",
      component: LoginView,
    },
    {
      path: "/reset-password",
      name: "reset-password",
      component: ForgetPassword,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/profile/payRes",
      name: "PaymentResponseView",
      component: PaymentResponseView,
    },
    {
      path: "/profile/privacypolicy",
      name: "PrivacyPolicy",
      component: PrivacyPolicy,
    },
    {
      path: "/profile/contact",
      name: "ContactUs",
      component: ContactUs,
    },
    {
      path: "/profile/termsofuse",
      name: "TermsView",
      component: TermsView,
    },
    {
      path: "/profile/InquiriesPolicy",
      name: "InquiriesPolicy",
      component: InquiriesPolicy,
    },
    {
      path: "/profile/ReturnPolicy",
      name: "ReturnPolicy",
      component: ReturnPolicy,
    },
    {
      path: "/profile/AccountStatusPage",
      name: "AccountStatusPage",
      component: AccountStatusPage,
    },
    {
      path: "/profile/residentialInfo",
      name: "ResidentialinfoView",
      component: ResidentialinfoView,
    },
    {
      path: "/profile/allInvoices",
      name: "AllInvoicesView",
      component: AllInvoicesView,
    },
    {
      path: "/profile/allInvoices/AnewPrint",
      name: "AnewPrint",
      component: AnewPrint,
    },
    {
      path: "/profile/personaldetails",
      name: "PersonalinfoView",
      component: PersonalinfoView,
    },
    {
      path: "/profile/CurrentPackage",
      name: "CurrentPackageView",
      component: CurrentPackageView,
    },
    {
      path: "/profile/account",
      name: "UserSettingsView",
      component: UserSettingsView,
    },
    {
      path: "/profile/attorney",
      name: "PowerofAttView",
      component: PowerofAttView,
    },
    {
      path: "/profile",
      name: "NProfileView",
      component: NProfileView,
    },
    {
      path: "/home",
      name: "userhome",
      component: UserHome,
    },
    {
      path: "/requests",
      name: "RequestsView",
      component: RequestsView,
    },
    {
      path: "/requests/requestDetails",
      name: "RequestDetails",
      component: RequestDetails,
    },
    {
      path: "/services",
      name: "ServicesView",
      component: ServicesView,
    },
    {
      path: "/packages",
      name: "PackagesView",
      component: PackagesView,
    },
    {
      path: "/packages/paynow",
      name: "Paynow",
      component: Paynow,
    },
    {
      path: "/loading",
      name: "loading",
      component: Loading,
    },
    {
      path: "/notifications",
      name: "Notifications",
      component: NotificationsView,
    },
    {
      path: "/services/study-case",
      name: "StudyCaseView",
      component: StudyCaseView,
    },
    {
      path: "/services/legal",
      name: "LegalServiceView",
      component: LegalServiceView,
    },
    {
      path: "/services/case",
      name: "CreateCaseView",
      component: CreateCaseView,
    },
    {
      path: "/services/consultation",
      name: "CreateConsultationView",
      component: CreateConsultationView,
    },
    {
      path: "/study-case-read/:id",
      name: "RequestFollowUp",
      component: RequestFollowUp,
      props: true,
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    // If navigating back, use the saved scroll position
    if (savedPosition) {
      return savedPosition;
    }

    // Only maintain scroll position for certain views (e.g., RequestsView, NotificationsView)
    const routesToMaintainScroll = ["RequestsView", "Notifications"];

    if (routesToMaintainScroll.includes(to.name)) {
      // Prevent scrolling to the top
      return false;
    }

    // For other routes, scroll to the top of the page
    return { top: 0 };
  },
});

export default router;
