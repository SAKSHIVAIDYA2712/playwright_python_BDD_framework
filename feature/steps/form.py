from behave import given, when, then
from page_models.formpage import FormPage


@given("the user is on the form page")
def on_form(context):
    form_page = FormPage(context, context.page)
    form_page.expect_navigation()


@when("the user enters valid form details and submits the form")
def enter_details(context):
    form_page = FormPage(context, context.page)
    form_page.fill_and_submit_form("sakshi vaidya", "sakshi.vaidya@atlascopco.com",
                                   "Female", "2002-12-27",
                                   "Pimple saudagar", context)


@then('a "Form successfully submitted" message should appear')
def submit_form(context):
    form_page = FormPage(context, context.page)
    if form_page.verify_success_message():
        return True
    else:
        print("form is incomplete")


@given("User is on login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given User is on login page')