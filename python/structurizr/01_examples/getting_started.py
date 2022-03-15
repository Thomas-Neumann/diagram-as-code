#!/usr/bin/env python3
"""
code copied and adapted from https://github.com/Midnighter/structurizr-python/blob/devel/examples/getting_started.py
Original Copyright: (c) 2020, Moritz E. Beber.
"""

# !! this creates 'getting_started.json' but it's unclear what to do
# !! with this file. Tried to load it on https://structurizr.com/dsl
# !! but the webpage expects a different file format
#
# tried to adopt https://github.com/Midnighter/structurizr-python/blob/devel/examples/upload_workspace.py
# but failed on line 22 (settings = StructurizrClientSettings()) with:
# -------------------------------------------------------
# pydantic.error_wrappers.ValidationError: 3 validation errors for StructurizrClientSettings
# workspace_id
#   field required (type=value_error.missing)
# api_key
#   field required (type=value_error.missing)
# api_secret
#   field required (type=value_error.missing)
# -------------------------------------------------------
#
# maybe this code no longer works with structurizr?

from structurizr import Workspace
from structurizr.model import Tags
from structurizr.view import ElementStyle, Shape
from structurizr.view.paper_size import PaperSize



def main() -> Workspace:
    """Create the 'getting started' example."""
    workspace = Workspace(
        name="Getting Started",
        description="This is a model of my software system.",
    )

    model = workspace.model

    user = model.add_person(name="User", description="A user of my software system.")
    software_system = model.add_software_system(
        name="Software System", description="My software system."
    )
    user.uses(software_system, "Uses")

    context_view = workspace.views.create_system_context_view(
        software_system=software_system,
        key="SystemContext",
        description="An example of a System Context diagram.",
    )
    context_view.add_all_elements()
    context_view.paper_size = PaperSize.A5_Landscape

    styles = workspace.views.configuration.styles
    styles.add(
        ElementStyle(tag=Tags.SOFTWARE_SYSTEM, background="#1168bd", color="#ffffff")
    )
    styles.add(
        ElementStyle(
            tag=Tags.PERSON,
            background="#08427b",
            color="#ffffff",
            shape=Shape.Person,
        )
    )
    return workspace


if __name__ == "__main__":
    diagram_file = "getting_started.json"

    print("Generating diagram.")
    workspace = main()

    print("Writing diagram file.")
    # unsure what to do with generated file
    workspace.dump(diagram_file, zip=False, indent=2)
