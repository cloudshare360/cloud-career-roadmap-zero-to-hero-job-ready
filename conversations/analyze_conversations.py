#!/usr/bin/env python3
"""
AI Conversation Analyzer

This script analyzes saved AI conversations to extract insights,
identify patterns, and create a structured learning plan.
"""

import os
import re
import json
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

class ConversationAnalyzer:
    def __init__(self, conversations_dir):
        self.conversations_dir = Path(conversations_dir)
        self.conversations = []
        self.analysis_results = {}
    
    def load_conversations(self):
        """Load all conversation files from the directory."""
        conversation_files = list(self.conversations_dir.glob("conversation_*.md"))
        
        for file_path in conversation_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    conversation = self.parse_conversation(content, file_path.name)
                    if conversation:
                        self.conversations.append(conversation)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        print(f"Loaded {len(self.conversations)} conversations")
    
    def parse_conversation(self, content, filename):
        """Parse a conversation markdown file."""
        sections = {
            'metadata': '',
            'question': '',
            'response': '',
            'takeaways': [],
            'action_items': [],
            'tags': []
        }
        
        # Extract sections using regex
        metadata_match = re.search(r'## Metadata\n(.*?)(?=##|$)', content, re.DOTALL)
        if metadata_match:
            sections['metadata'] = metadata_match.group(1).strip()
        
        question_match = re.search(r'## Question/Query\n(.*?)(?=##|$)', content, re.DOTALL)
        if question_match:
            sections['question'] = question_match.group(1).strip()
        
        response_match = re.search(r'## AI Response/Solution\n(.*?)(?=##|$)', content, re.DOTALL)
        if response_match:
            sections['response'] = response_match.group(1).strip()
        
        # Extract takeaways
        takeaways_match = re.search(r'## Key Takeaways\n(.*?)(?=##|$)', content, re.DOTALL)
        if takeaways_match:
            takeaways_text = takeaways_match.group(1)
            sections['takeaways'] = re.findall(r'- \[(.*?)\]', takeaways_text)
        
        # Extract tags
        tags_match = re.findall(r'`#(\w+)`', content)
        sections['tags'] = tags_match
        
        # Extract topic category from metadata
        topic_match = re.search(r'Topic Category.*?:\s*(.*)', sections['metadata'])
        topic_category = topic_match.group(1).strip() if topic_match else 'Unknown'
        
        return {
            'filename': filename,
            'topic_category': topic_category,
            'sections': sections
        }
    
    def analyze_topics(self):
        """Analyze conversation topics and categories."""
        topic_counter = Counter()
        tag_counter = Counter()
        
        for conv in self.conversations:
            topic_counter[conv['topic_category']] += 1
            tag_counter.update(conv['sections']['tags'])
        
        self.analysis_results['topics'] = dict(topic_counter)
        self.analysis_results['tags'] = dict(tag_counter)
    
    def identify_learning_paths(self):
        """Identify potential learning paths based on conversation topics."""
        # Group conversations by topic category
        topic_groups = defaultdict(list)
        for conv in self.conversations:
            topic_groups[conv['topic_category']].append(conv)
        
        learning_paths = {}
        for topic, conversations in topic_groups.items():
            learning_paths[topic] = {
                'conversation_count': len(conversations),
                'conversations': [conv['filename'] for conv in conversations],
                'key_concepts': []
            }
            
            # Extract key concepts from questions and responses
            all_text = ' '.join([
                conv['sections']['question'] + ' ' + conv['sections']['response']
                for conv in conversations
            ])
            
            # Simple keyword extraction (can be enhanced with NLP)
            common_words = self.extract_keywords(all_text)
            learning_paths[topic]['key_concepts'] = common_words[:10]
        
        self.analysis_results['learning_paths'] = learning_paths
    
    def extract_keywords(self, text):
        """Extract important keywords from text."""
        # Remove common stop words and extract meaningful terms
        stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those', 'a', 'an'}
        
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        filtered_words = [word for word in words if word not in stop_words]
        
        return [word for word, count in Counter(filtered_words).most_common(10)]
    
    def create_roadmap(self):
        """Create a learning roadmap based on analysis."""
        roadmap = {
            'overview': {
                'total_conversations': len(self.conversations),
                'topics_covered': len(self.analysis_results.get('topics', {})),
                'analysis_date': datetime.now().isoformat()
            },
            'learning_phases': [],
            'recommended_sequence': []
        }
        
        # Define typical cloud career progression
        progression_order = [
            'Fundamentals',
            'Cloud Computing',
            'Infrastructure',
            'DevOps',
            'Security',
            'Advanced Topics',
            'Career Development'
        ]
        
        topics = self.analysis_results.get('topics', {})
        learning_paths = self.analysis_results.get('learning_paths', {})
        
        for phase in progression_order:
            matching_topics = [topic for topic in topics.keys() 
                             if any(keyword in topic.lower() for keyword in phase.lower().split())]
            
            if matching_topics:
                phase_info = {
                    'phase': phase,
                    'topics': matching_topics,
                    'conversations': sum(topics[topic] for topic in matching_topics),
                    'priority': 'High' if any(topics[topic] > 2 for topic in matching_topics) else 'Medium'
                }
                roadmap['learning_phases'].append(phase_info)
        
        self.analysis_results['roadmap'] = roadmap
    
    def generate_report(self):
        """Generate a comprehensive analysis report."""
        self.analyze_topics()
        self.identify_learning_paths()
        self.create_roadmap()
        
        # Save analysis results
        output_file = self.conversations_dir / 'analysis_report.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.analysis_results, f, indent=2)
        
        # Generate markdown report
        self.generate_markdown_report()
        
        print(f"Analysis complete! Results saved to {output_file}")
    
    def generate_markdown_report(self):
        """Generate a markdown report."""
        report_content = f"""# AI Conversations Analysis Report

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
- **Total Conversations**: {len(self.conversations)}
- **Topics Covered**: {len(self.analysis_results.get('topics', {}))}
- **Unique Tags**: {len(self.analysis_results.get('tags', {}))}

## Topic Distribution
"""
        
        topics = self.analysis_results.get('topics', {})
        for topic, count in sorted(topics.items(), key=lambda x: x[1], reverse=True):
            report_content += f"- **{topic}**: {count} conversations\n"
        
        report_content += "\n## Most Common Tags\n"
        tags = self.analysis_results.get('tags', {})
        for tag, count in sorted(tags.items(), key=lambda x: x[1], reverse=True)[:10]:
            report_content += f"- `#{tag}`: {count} times\n"
        
        report_content += "\n## Learning Roadmap\n"
        roadmap = self.analysis_results.get('roadmap', {})
        for phase in roadmap.get('learning_phases', []):
            report_content += f"\n### {phase['phase']} (Priority: {phase['priority']})\n"
            report_content += f"- Conversations: {phase['conversations']}\n"
            report_content += f"- Topics: {', '.join(phase['topics'])}\n"
        
        report_content += "\n## Recommendations\n"
        report_content += "1. Focus on topics with the highest conversation count first\n"
        report_content += "2. Create practical projects for each learning phase\n"
        report_content += "3. Set up hands-on labs for technical topics\n"
        report_content += "4. Join communities related to your most discussed tags\n"
        
        report_file = self.conversations_dir / 'analysis_report.md'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)

def main():
    """Main function to run the analysis."""
    conversations_dir = os.path.dirname(os.path.abspath(__file__))
    analyzer = ConversationAnalyzer(conversations_dir)
    
    print("Loading conversations...")
    analyzer.load_conversations()
    
    if analyzer.conversations:
        print("Generating analysis report...")
        analyzer.generate_report()
        print("Analysis complete!")
    else:
        print("No conversations found. Please add conversation files using the template.")

if __name__ == "__main__":
    main()