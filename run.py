from app import create_app
app = create_app()

# print("🔍 Registered routes:")
# for rule in app.url_map.iter_rules():
#     print(f"{rule.rule} → Methods: {list(rule.methods)}")
for rule in app.url_map.iter_rules():
    print(f"{rule.rule} → Methods: {list(rule.methods)}")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
