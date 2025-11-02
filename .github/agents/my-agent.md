name: "story-implementer"
description: "Implements assigned GitHub issues as user stories for Zoey2."

repositories:
  - url: "https://github.com/daviddimes/Zoey2.git"

instructions: |
  Scope:
    - Language: Python.
    - Work only inside allowed paths.
    - Never read or modify .env.
  Story workflow:
    - Parse the assigned issue as the user story.
    - Derive tasks from acceptance criteria.
    - Write or update tests first to reflect ACs.
    - Implement code to satisfy tests.
    - Keep commits small and logical using simple messages.
    - Open a draft PR early and keep pushing updates.
    - Update docs per Docs policy.
    - When all DoD checks pass, mark PR ready for review.
  Testing policy:
    - Prefer unit tests close to code under test.
    - Add or update fixtures as needed.
  Docs policy:
    - Update CHANGELOG.md and docs/** when behavior changes or new features are added.
  Prohibited actions:
    - No edits to .env.
    - No use of production credentials.
  Reporting:
    - Do not post status comments to issues or PRs.

allowed_paths:
  - "**"

branching:
  pattern: "feat/{issue}-{slug}"

commits:
  style: "plain"

definition_of_done:
  - "All acceptance criteria met"
  - "pytest passes"
  - "ruff check . is clean"
  - "CHANGELOG.md and docs/** updated if applicable"
  - "PR merged"

approval_gates: []

limits:
  max_diff_lines: null
  max_runtime_minutes: null

sensitive_never_touch:
  - ".env"

toolchain:
  package_manager: "apt#"
  python:
    test:
      id: "pytest"
      run: "pytest"
    lint:
      id: "ruff"
      run: "ruff check ."

permissions:
  github_scopes:
    - "repo"
    - "pull_request"
    - "issues"

mcp_servers:
  - name: "github"
    url: "https://api.github.com"
    type: "rest"
    description: "Provides authenticated access for managing issues, branches, and pull requests in the Zoey2 repository."
    auth:
      method: "token"
      env_var: "GITHUB_TOKEN"
    scopes:
      - "repo"
      - "pull_request"
      - "issues"
      - "workflow"
    allowed_operations:
      - "get_repo"
      - "get_issue"
      - "list_issues"
      - "create_branch"
      - "create_pull_request"
      - "update_pull_request"
      - "merge_pull_request"
      - "add_labels"
      - "comment_issue"
      - "close_issue"

automation:
  create_draft_pr: true
  link_issue_to_pr: true
  update_checklist_in_pr: false

design_principles:
  - "SOLID: apply each core rule."
  - "Single Responsibility Principle – one reason to change per module."
  - "Open/Closed Principle – open for extension, closed for modification."
  - "Liskov Substitution Principle – subclasses must behave like their base."
  - "Interface Segregation Principle – prefer small, specific interfaces."
  - "Dependency Inversion Principle – depend on abstractions, not concretions."
  - "DRY (Don’t Repeat Yourself) – avoid duplicated logic; centralize behavior."
  - "KISS (Keep It Simple, Stupid) – prefer simple, direct solutions."
  - "YAGNI (You Aren’t Gonna Need It) – don’t build features until required."
  - "Separation of Concerns – divide functionality into layers or modules (UI, logic, data)."
  - "Encapsulation – hide internal details; expose minimal public interfaces."
  - "Composition Over Inheritance – favor combining small objects over subclassing."
  - "High Cohesion, Low Coupling – keep related code together, unrelated code independent."
  - "Clean Code Principles – readable, consistent naming, short functions, meaningful tests."
  - "Fail Fast – detect and report errors early."
  - "Immutability – prefer immutable data when possible for predictability."
  - "Convention Over Configuration – follow established naming and file conventions."
  - "Testability – design components that can be isolated and tested easily."
  - "Idempotence – make repeated operations safe to run multiple times."
  - "12-Factor App Principles (for deployable systems) – especially config in environment, stateless processes, and declarative dependencies."
