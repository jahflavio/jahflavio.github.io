import re
from generate_cvs_extra import data_general_es, data_general_en

def generate_jobs_html(data):
    html = ""
    for i, job in enumerate(data['exp']):
        html += f'''                <!-- Job {i+1} -->
                <div class="editorial-job">
                    <div class="job-header">
                        <h3 class="job-role">{job['title']}</h3>
                        <span class="job-date">{job['date']}</span>
                    </div>
                    <p class="job-company">{job['company']}</p>
                    <ul class="job-list">
'''
        for bullet in job['bullets']:
            html += f'                        <li>{bullet}</li>\n'
        html += '''                    </ul>
                </div>\n\n'''
    return html.strip()

def sync_file(filename, data, lang='es'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Profile text
    profile_pattern = re.compile(r'(<p class="hero-subtitle hero-text">)(.*?)(</p>)', re.DOTALL)
    content = profile_pattern.sub(r'\1' + data['profile'] + r'\3', content, count=1)
    
    # 2. Update role tags underneath (optional, but let's leave it as is if it's fine, or update it)
    # The role tags in CV are "Digital Marketing, SEO, Front End, UX/UI"
    role_pattern = re.compile(r'(<p class="hero-subtitle hero-text" style=".*?>)(.*?)(</p>)', re.DOTALL)
    roles_text = " | ".join(data['role'].split(', '))
    content = role_pattern.sub(r'\1' + roles_text + r'\3', content, count=1)
    
    # 3. Update the experience section
    exp_pattern = re.compile(r'(<!-- Job 1 -->).*?(</div>\s*</div>\s*<!-- Right Column: Skills & Education -->)', re.DOTALL)
    
    new_jobs_html = generate_jobs_html(data)
    
    # also update the section-count
    count_pattern = re.compile(r'(<span class="section-count">)\d+ roles(</span>)')
    content = count_pattern.sub(r'\g<1>' + str(len(data['exp'])) + r' roles\2', content)
    
    # put it together
    replacement = new_jobs_html + '\n            </div>\n\n            <!-- Right Column: Skills & Education -->'
    content = exp_pattern.sub(replacement, content)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if __name__ == '__main__':
    sync_file('index.html', data_general_es, 'es')
    sync_file('index-en.html', data_general_en, 'en')
