const form = document.querySelector("#form__wrap"); // 데이터를 전송하는 폼
const checkAll = document.querySelector(".terms__check__all input"); // 모두 동의 체크박스
const checkBoxes = document.querySelectorAll(".input__check input"); // 모두 동의를 제외한 박스
const submitButton = document.querySelector("button"); // 확인버튼

const agreements = {
  termsOfService: false, // 첫번째 필수동의
  privacyPolicy: false, // 두번째 필수동의 
  allowPromotions: false // 세번째 수신동의
};

form.addEventListener("submit", (e) => e.preventDefault());

checkBoxes.forEach((item) => item.addEventListener("input", toggleCheckbox));

function toggleCheckbox(e) {
  const { checked, id } = e.target; //e.target.checked && e.target.id
  agreements[id] = checked;
  this.parentNode.classList.toggle("active");
  checkAllStatus();
  toggleSubmitButton();
}

function checkAllStatus() {
  const { termsOfService, privacyPolicy, allowPromotions } = agreements;
  if (termsOfService && privacyPolicy && allowPromotions) {
    checkAll.checked = true;
  } else {
    checkAll.checked = false;
  }
}

function toggleSubmitButton() {
  const { termsOfService, privacyPolicy } = agreements;
  if (termsOfService && privacyPolicy) {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}

checkAll.addEventListener("click", (e) => {
  const { checked } = e.target;
  if (checked) {
    checkBoxes.forEach((item) => {
      item.checked = true;
      agreements[item.id] = true;
      item.parentNode.classList.add("active");
    });
  } else {
    checkBoxes.forEach((item) => {
      item.checked = false;
      agreements[item.id] = false;
      item.parentNode.classList.remove("active");
    });
  }
  toggleSubmitButton();
});
