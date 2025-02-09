def integrate_modules(main_block, modules):
    """
    Integrates the main block with the modular blocks based on their interface definitions.

    :param main_block: The main content block of the document (not null).
    :param modules: A list of modular blocks to be integrated into the document.
    :return: The fully integrated document.
    """
    def resolve_interface(module):
        """
        Extracts the interface information from the module.

        If the module contains multiple interfaces, use the first one to determine placement.
        Alternatively, a dedicated property can define the module's placement.

        :param module: A modular block containing interface definitions.
        :return: A tuple of position and parameters for placement, or default values if undefined.
        """
        interfaces = module.get('interface', [])
        if isinstance(interfaces, list) and interfaces:
            return interfaces[0].get('position', float('inf')), interfaces[0].get('params', {})
        elif isinstance(interfaces, dict):
            return interfaces.get('position', float('inf')), interfaces.get('params', {})
        return float('inf'), {}

    try:
        # Sort modules based on their interface position for proper integration order
        sorted_modules = sorted(modules, key=lambda mod: resolve_interface(mod)[0])

        # Integrate sorted modules into the main block
        integrated_document = main_block
        for module in sorted_modules:
            position, params = resolve_interface(module)
            if position != float('inf'):
                # Use the joinDoc function to attach each module to the main block
                integrated_document = joinDoc(integrated_document, [module])
            else:
                # Log a warning or handle modules without a valid position
                print(f"Warning: Module skipped due to missing or invalid position: {module}")

        return integrated_document

    except Exception as e:
        print(f"Error during integration: {e}")
        raise

# Example use
if __name__ == "__main__":
    def joinDoc(main_block, modules):
        """
        Mock implementation of joinDoc to simulate document integration.

        :param main_block: The main content block.
        :param modules: List of modules to join.
        :return: Integrated document as a dictionary.
        """
        for module in modules:
            main_block['content'] += f"\n{module.get('content', '')}"
        return main_block

    # Mock data
    main_block = {"content": "Main Document"}
    modules = [
        {"interface": [{"position": 2, "params": {"title": "Second Section"}}], "content": "Content of module 2"},
        {"interface": [{"position": 1, "params": {"title": "First Section"}}], "content": "Content of module 1"},
        {"content": "Content of module without interface"}  # Example of missing interface
    ]

    try:
        # Integrated document
        integrated_document = integrate_modules(main_block, modules)
        print("Integrated Document:")
        print(integrated_document)
    except Exception as e:
        print(f"Failed to integrate modules: {e}")
