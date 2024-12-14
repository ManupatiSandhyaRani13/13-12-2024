import streamlit as st
class Bank:
    def __init__(self):
        if 'bal' not in st.session_state:
            st.session_state.bal = 100000  # Initial balance
        if 'pin_verified' not in st.session_state:
            st.session_state.pin_verified = False
        if 'pin_attempts' not in st.session_state:
            st.session_state.pin_attempts = 0  # Track PIN attempts
    def deposit(self):
        amt = st.number_input("Enter the deposit amount:", min_value=0, max_value=50000)
        if st.button('Deposit'):
            if 100 <= amt <= 50000 and amt % 100 == 0:
                st.session_state.bal += amt
                st.success(f'Total balance is: {st.session_state.bal}')
            else:
                st.error(
                    'Minimum deposit is 100, maximum deposit is 50000, and the machine accepts only 100 INR notes.')
    def withdraw(self):
        withdraw_amt = st.number_input("Enter the withdrawal amount:", min_value=100, max_value=20000)
        if st.button('Withdraw'):
            if withdraw_amt > st.session_state.bal:
                st.error('Insufficient balance to complete the withdrawal.')
            elif withdraw_amt % 100 != 0:
                st.error('The machine dispenses only 100 INR notes.')
            else:
                st.session_state.bal -= withdraw_amt
                st.success(f'Available balance is: {st.session_state.bal}')
    def balEnquiry(self):
        st.info(f'Your current balance is: {st.session_state.bal}')
    def viewOptions(self):
        option = st.selectbox("Choose an option", ["Deposit", "Withdraw", "Balance Enquiry", "Exit"])
        if option == "Deposit":
            self.deposit()
        elif option == "Withdraw":
            self.withdraw()
        elif option == "Balance Enquiry":
            self.balEnquiry()
        elif option == "Exit":
            st.write("Thank you for using ABC Bank. Have a great day!")
            st.session_state.pin_verified = False
    def validation(self):
        if not st.session_state.pin_verified:
            st.title('Welcome to ABC Bank')
            userPin = st.number_input('Enter PIN:', min_value=0, max_value=9999, step=1)

            if st.button("Check PIN"):
                if userPin == 1234:
                    st.session_state.pin_verified = True
                    st.success("PIN verified. You can now access your account.")
                else:
                    st.session_state.pin_attempts += 1
                    if st.session_state.pin_attempts >= 3:
                        st.error('Too many failed attempts. Please try again later.')
                        st.session_state.pin_verified = False
                    else:
                        st.error('Invalid PIN. Please try again.')
        if st.session_state.pin_verified:
            self.viewOptions()
obj = Bank()
obj.validation()


