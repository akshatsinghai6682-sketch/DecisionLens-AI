import React from 'react';
import { Zap, Users, BarChart3, Map, Lightbulb } from 'lucide-react';

export const Features: React.FC = () => {
  const features = [
    {
      icon: <Zap size={32} className="text-blue-600" />,
      title: 'Diagnostic Conversation',
      description: 'AI guides you through 5 key diagnostic questions to understand your values and constraints.',
    },
    {
      icon: <Users size={32} className="text-purple-600" />,
      title: 'Perspective Panel',
      description: '5 advisor archetypes provide diverse viewpoints on your decision from different angles.',
    },
    {
      icon: <BarChart3 size={32} className="text-green-600" />,
      title: 'Scenario Simulation',
      description: 'Explore best, expected, and worst case scenarios with detailed financial and lifestyle analysis.',
    },
    {
      icon: <Map size={32} className="text-orange-600" />,
      title: 'Uncertainty Mapping',
      description: 'Understand what you know, what you don\'t know, and what you\'re assuming.',
    },
    {
      icon: <Lightbulb size={32} className="text-yellow-600" />,
      title: 'Hidden Tradeoffs',
      description: 'Discover tradeoffs you might not have considered that could swing your decision.',
    },
    {
      icon: <Zap size={32} className="text-red-600" />,
      title: 'Clarity Report',
      description: 'Export a comprehensive PDF report with all insights and recommendations.',
    },
  ];

  return (
    <div className="py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-4xl font-bold text-gray-900 mb-4 text-center">How It Works</h2>
        <p className="text-center text-gray-600 mb-12">DecisionLens AI helps you think through complex life decisions</p>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, idx) => (
            <div key={idx} className="bg-white rounded-lg shadow-lg p-6 hover:shadow-xl transition">
              <div className="mb-4">{feature.icon}</div>
              <h3 className="text-xl font-bold text-gray-900 mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
